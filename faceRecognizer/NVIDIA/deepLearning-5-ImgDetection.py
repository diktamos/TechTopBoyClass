import jetson.inference
import jetson.utils
import time
import cv2
import numpy as np

fpsFilter = 0


#cam = jetson.utils.gstCamera(640,512,"/dev/video1")
cam = jetson.utils.gstCamera(0)
disp = jetson.utils.glDisplay()
font = jetson.utils.cudaFont()

net = jetson.inference.detectNet('ssd-mobilenet-v2',threshold=.5)
timeStamp = time.time()
while disp.IsOpen():
    frame, width, height = cam.CaptureRGBA()
    detections = net.Detect(frame,width,height)
    
    dt = time.time()-timeStamp
    timeStamp = time.time()
    fps = 1/dt
    fpsFilter = 0.9*fpsFilter + 0.1*fps
    print(str(round(fpsFilter,1))+' fps')
         
    disp.RenderOnce(frame,width,height)
