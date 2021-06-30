import jetson.inference
import jetson.utils
import time
import cv2
import numpy as np


width = 640
height = 512

dispW = width
dispH = height
flip=0

#cam = jetson.utils.gstCamera(width,height,1)
#camSet='nvarguscamerasrc !  video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=21/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(width)+', height='+str(height)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'
#camSet='nvarguscamerasrc wbmode=daylight tnr-mode=1 tnr-strength=1 ee-mode=2 ee-strength=1 !  video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=21/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(dispW)+', height='+str(dispH)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! videobalance contrast=1.5 brightness=-.15 saturation=1.2 ! appsink drop=true'
#cam1 = cv2.VideoCapture(camSet)

camNumber = 1
#cam=cv2.VideoCapture(camSet)
cam1 = cv2.VideoCapture(camNumber)

#if internet cam

#cam1 = cv2.VideoCapture(1)
#cam1.set(cv2.CAP_PROP_FRAME_WIDTH,dispW)
#cam1.set(cv2.CAP_PRO_FRAME_HEIGHT,dispH)


#net = jetson.inference.imageNet('googlenet',['--model=/home/jetson/Downloads/jetson-inference/python/training/classification/myModel/resnet18.onnx','--input_blob=input_0','--output_blob=output_0','--labels=/home/jetson/Downloads/jetson-inference/myTrain/labels.txt'])
net = jetson.inference.imageNet('alexnet',['--model=/home/jetson/Downloads/jetson-inference/python/training/classification/myModelGame/resnet18.onnx','--input_blob=input_0','--output_blob=output_0','--labels=/home/jetson/Downloads/jetson-inference/myTrain/labels.txt'])

font = cv2.FONT_ITALIC

timeMark = time.time()
fpsFilter = 0

while True:
    #frame, width, height = cam.CaptureRGBA(zeroCopy=1)
    _, frame = cam1.read()
    img = cv2.cvtColor(frame,cv2.COLOR_BGR2RGBA).astype(np.float32)
    img = jetson.utils.cudaFromNumpy(img)
    classID, confidence = net.Classify(img,width,height)
    item = net.GetClassDesc(classID)
    dt = time.time() -timeMark
    fps = 1/dt
    fpsFilter = 0.95*fpsFilter+0.05*fps
    fpsFilterStr = str(round(fpsFilter,1))+' fps; '
    timeMark = time.time()
    #font.OverlayText(frame,width,height,fpsFilterStr+item,5,5,font.Magenta,font.Blue)
    #display.RenderOnce(frame,width,height)
    #frame=jetson.utils.cudaToNumpy(frame,width,height,4)
    #frame = cv2.cvtColor(frame,cv2.COLOR_RGBA2BGR).astype(np.uint8)

    cv2.putText(frame,fpsFilterStr+item,(0,30),font,1,(0,0,255),2)
    cv2.imshow('recCam',frame)
    cv2.moveWindow('recCam',0,0)

    if cv2.waitKey(1)==ord('q'):
        break

cam1.release()
cv2.destroyAllWindows()