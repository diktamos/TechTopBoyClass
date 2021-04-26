import cv2
print('cv2 version:', cv2.__version__)
import numpy as np

def nothing(x):
    pass

dispW = 640 #640
dispH = 480 #512
flip=0

cv2.namedWindow('Trackbars')
cv2.moveWindow('Trackbars',1320,0)


cv2.createTrackbar('hueLow','Trackbars',9,179,nothing)
cv2.createTrackbar('hueHigh','Trackbars',25,179,nothing)
cv2.createTrackbar('hue2Low','Trackbars',130,179,nothing)
cv2.createTrackbar('hue2High','Trackbars',100,179,nothing)

cv2.createTrackbar('satLow','Trackbars',100,255,nothing)
cv2.createTrackbar('satHigh','Trackbars',255,255,nothing)

cv2.createTrackbar('valLow','Trackbars',100,255,nothing)
cv2.createTrackbar('valHigh','Trackbars',255,255,nothing)





#for rasbery pi camera

camSet='nvarguscamerasrc !  video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=21/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(dispW)+', height='+str(dispH)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'

#camNumber = 0
cam=cv2.VideoCapture(camSet)

#cam = cv2.VideoCapture(camNumber)
while True:
    ret,frame = cam.read()
    #frame = cv2.imread('smarties.png')
 
    cv2.imshow('Rassbery camera',frame)
    cv2.moveWindow('Rassbery camera',0,0)
    
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    hueLow = cv2.getTrackbarPos('hueLow','Trackbars')
    hueUp = cv2.getTrackbarPos('hueHigh','Trackbars')

    hue2Low = cv2.getTrackbarPos('hue2Low','Trackbars')
    hue2Up = cv2.getTrackbarPos('hue2High','Trackbars')

    satLow = cv2.getTrackbarPos('satLow','Trackbars')
    satUp = cv2.getTrackbarPos('satHigh','Trackbars')

    valLow = cv2.getTrackbarPos('valLow','Trackbars')
    valUp = cv2.getTrackbarPos('valHigh','Trackbars')

    l_b = np.array([hueLow,satLow,valLow])
    u_b = np.array([hueUp,satUp,valUp])

    l_b2 = np.array([hue2Low,satLow,valLow])
    u_b2 = np.array([hue2Up,satUp,valUp])
    #print('l_b = ',l_b)
    #print('u_b = ',u_b)

    FGmask = cv2.inRange(hsv,l_b,u_b)
    FGmask2 = cv2.inRange(hsv,l_b2,u_b2)
    FGmaskComp = cv2.add(FGmask,FGmask2)
    cv2.imshow('FGmaskComp)',FGmaskComp)
    cv2.moveWindow('FGmaskComp)',0,410)

    contours,_= cv2.findContours(FGmaskComp,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    contours = sorted(contours,key=lambda x: cv2.contourArea(x),reverse=True)

    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area >= 50:
          #  cv2.drawContours(frame,[cnt],0,(255,0,0),2)
            (x,y,w,h) = cv2.boundingRect(cnt)
            cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),3)


    cv2.drawContours(frame,contours,0,(255,0,255),0)

    cv2.imshow('Rassbery camera',frame)
    cv2.moveWindow('Rassbery camera',0,0)

    if cv2.waitKey(1)==ord('q'):
        break

cam.release()
cv2.destroyAllWindows()