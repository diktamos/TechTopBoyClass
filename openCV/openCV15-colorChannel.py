import cv2
import numpy as np
print('cv2 version:', cv2.__version__)
dispW = 320 #640
dispH = 240 #512
flip=0

#for rasbery pi camera

camSet='nvarguscamerasrc !  video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=21/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(dispW)+', height='+str(dispH)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'

#camNumber = 0
cam=cv2.VideoCapture(camSet)
blank = np.zeros([240,320,1],np.uint8)
#blank[0:480,0:320] = 255
#cam = cv2.VideoCapture(camNumber)
while True:
    ret,frame = cam.read()
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    print(frame[50,45,1])
    print('frame shape: ',frame.shape)
    print('frame gray: ',gray.shape)
    print('frame.size = ',frame.size)
    print('gray.size = ',frame.size)
    b,g,r = cv2.split(frame)

    blue = cv2.merge((b,blank,blank))
    green = cv2.merge((blank,g,blank))
    red = cv2.merge((blank,blank,r))
    #g[:] = g[:]*0.2
    merge = cv2.merge((b,g,r))

  
     # print('ret: ',ret)
    cv2.imshow('Rassbery camera',frame)
    cv2.moveWindow('Rassbery camera',0,0)

    cv2.imshow('blue',blue)
    cv2.moveWindow('blue',400,0)

    cv2.imshow('red',red)
    cv2.moveWindow('red',0,320)

    cv2.imshow('green',green)
    cv2.moveWindow('green',400,320)

    cv2.imshow('blank', blank)
    cv2.moveWindow('blank',800,0)

    cv2.imshow('merge', merge)
    cv2.moveWindow('merge',800,320)

    if cv2.waitKey(1)==ord('q'):
        break

cam.release()
cv2.destroyAllWindows()