import cv2
import numpy as np
import time

print('cv2 version:', cv2.__version__)
dispW = 640 #640
dispH = 480 #512
flip=0
font=cv2.FONT_HERSHEY_SIMPLEX
dtav = 0


camSet='nvarguscamerasrc !  video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=21/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(dispW)+', height='+str(dispH)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'
cam1=cv2.VideoCapture(camSet)

camNumber = 1
cam2 = cv2.VideoCapture(camNumber)
startTime = time.time()
while True:
    ret,frame1 = cam1.read()
    ret,frame2 = cam2.read()
    print("size cam1:", frame1.shape)
    print("size cam2:", frame2.shape)
    h,w = frame1.shape[0],frame1.shape[1]
    print(h,w)
    frame2 = cv2.resize(frame2,(w,h))
    frameCombined = np.hstack((frame1,frame2))
    #cv2.imshow('Rassbery camera',frame1)
    #cv2.moveWindow('Rassbery camera',0,0)

    #cv2.imshow('FLIR camera',frame2)
    #cv2.moveWindow('FLIR camera',0,500)
    dt = time.time()-startTime
    dtav = 0.9*dtav + 0.1*dt
    fps = str(round(1/dtav,1))+" fps"
    startTime = time.time()


    cv2.rectangle(frameCombined,(0,0),(130,40),(30,50,0),-1)
    cv2.putText(frameCombined,fps,(0,25),font,0.6,(200,200,0),2)
    cv2.imshow('Combo',frameCombined)
    cv2.moveWindow('Combo',0,0)

   



    if cv2.waitKey(1)==ord('q'):
        break

cam.release()
cv2.destroyAllWindows()