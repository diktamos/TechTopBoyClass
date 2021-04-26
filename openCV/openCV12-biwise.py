import cv2
import numpy as np
print('cv2 version:', cv2.__version__)
dispW = 640
dispH = 512
flip = 2

img1 = np.zeros((dispH,dispW,1), np.uint8)
img1[0:dispH,0:320] = [255]
img2 = np.zeros((dispH,dispW,1),np.uint8)
img2[190:290,290:370] = [255]

bitAND = cv2.bitwise_and(img1,img2)
bitOR = cv2.bitwise_or(img1,img2)
bitXOR = cv2.bitwise_xor(img1,img2)


'''
#for rasbery pi camera
camSet='nvarguscamerasrc !  video/x-raw(memory:NVMM), \
        width=3264, height=2464, format=NV12, framerate=21/1 ! \
        nvvidconv flip-method='+str(flip)+' ! \
        video/x-raw, width='+str(dispW)+', \
        height='+str(dispH)+', format=BGRx !\
        videoconvert ! video/x-raw, format=BGR ! \
        appsink'
'''
camNumber = 0
#cam=cv2.VideoCapture(camSet)
cam = cv2.VideoCapture(camNumber)
while True:
    ret,frame = cam.read()
    
    cv2.imshow('img1',img1)
    cv2.moveWindow('img1',0,500)

    cv2.imshow('img2',img2)
    cv2.moveWindow('img2',700,0)

    cv2.imshow('AND',bitAND)
    cv2.moveWindow('AND',700,500)

    cv2.imshow('OR',bitOR)
    cv2.moveWindow('OR',1200,500)

    cv2.imshow('XOR',bitXOR)
    cv2.moveWindow('XOR',1200,0)

    frame=cv2.bitwise_and(frame,frame,mask=bitXOR)
    cv2.imshow('FLIRcamera',frame)
    cv2.moveWindow('FLIRcamera',0,0)
    if cv2.waitKey(1)==ord('q'):
        break

cam.release()
cv2.destroyAllWindows()