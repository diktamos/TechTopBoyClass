import cv2
print('cv2 version:', cv2.__version__)
dispW=int(640*1)
dispH=int(480*1)
flip=2

camNumber = 0
#cam=cv2.VideoCapture(camSet)
cam=cv2.VideoCapture(camNumber)
#cam.set(cv2.CAP_PROP_FRAME_WIDTH,dispW)
#cam.set(cv2.CAP_PROP_FRAME_HEIGHT,dispH)
while True:
    ret,frame = cam.read()
    frame = cv2.resize(frame,(dispW,dispH))
    
    print(cam.get(cv2.CAP_PROP_FRAME_WIDTH))
       
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    
    cv2.imshow('FLIRcamera',frame)
    cv2.moveWindow('FLIRcamera',0,0)
    
    cv2.imshow('grayVideo',gray)
    cv2.moveWindow('grayVideo',0,dispH+60)
   
    
   
    if cv2.waitKey(1)==ord('q'):
        break

cam.release()
cv2.destroyAllWindows()