import jetson.inference
import jetson.utils
import time
import cv2
import numpy as np

width = 1280
height = 720

dispW = width
dispH = height
flip=0

fpsFilter = 0
font = cv2.FONT_ITALIC


camSet='nvarguscamerasrc wbmode=daylight tnr-mode=1 tnr-strength=1 ee-mode=2 ee-strength=1 !  video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=21/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(dispW)+', height='+str(dispH)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! videobalance contrast=1.5 brightness=-.15 saturation=1.2 ! appsink'
cam=cv2.VideoCapture(camSet)

'''
cam = cv2.VideoCapture("/dev/video1")
cam.set(cv2.CAP_PROP_FRAME_WIDTH,dispW)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,dispH)
'''
net = jetson.inference.detectNet('ssd-mobilenet-v2',threshold=.5)
timeStamp = time.time()
while True:
    _,frame = cam.read()
    height = frame.shape[0]
    width = frame.shape[1]

    img = cv2.cvtColor(frame,cv2.COLOR_RGBA2BGR).astype(np.float32)
    img = jetson.utils.cudaFromNumpy(frame)

    detections = net.Detect(img,width,height)
    
    for detect in detections:
        #print(detect)
        ID = detect.ClassID
        item = net.GetClassDesc(ID)
        left = detect.Left
        bottom = detect.Bottom
        right = detect.Right

        print(ID,":",item, left,bottom, right)

    
    dt = time.time()-timeStamp
    timeStamp = time.time()
    fps = 1/dt
    fpsFilter = 0.9*fpsFilter + 0.1*fps
    #print(str(round(fpsFilter,1))+' fps')
         
    
    cv2.putText(frame,str(round(fpsFilter,1))+' fps',(0,30),font,1,(200,100,0),2)
    cv2.imshow('detCame',frame)
    cv2.moveWindow('detCame',0,0)

    if cv2.waitKey(1)==ord('q'):
        break

cam.release()
cv2.destroyAllWindows()
