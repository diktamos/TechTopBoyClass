import jetson.inference
import jetson.utils
import time
import cv2
import numpy as np


width = 1280
height = 720

#cam = jetson.utils.gstCamera(width,height,1)
cam = jetson.utils.gstCamera(0)

display = jetson.utils.glDisplay()
net = jetson.inference.imageNet('googlenet')

font = jetson.utils.cudaFont()

timeMark = time.time()
fpsFilter = 0

while display.IsOpen():
    frame, width, height = cam.CaptureRGBA(zeroCopy=1)
    
    classID, confidence = net.Classify(frame,width,height)
    item = net.GetClassDesc(classID)
    dt = time.time() -timeMark
    fps = 1/dt
    fpsFilter = 0.95*fpsFilter+0.05*fps
    fpsFilterStr = str(round(fpsFilter,1))+' fps; '
    timeMark = time.time()
    font.OverlayText(frame,width,height,fpsFilterStr+item,5,5,font.Magenta,font.Blue)
    display.RenderOnce(frame,width,height)

