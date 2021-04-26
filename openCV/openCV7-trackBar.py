import cv2
print('cv2 version:', cv2.__version__)
dispW = 640
dispH = 512
flip=2
def nothing(x):
    pass
camNumber = 0
#cam=cv2.VideoCapture(camSet)
cam = cv2.VideoCapture(camNumber)
cv2.namedWindow('FLIRcamera')
cv2.createTrackbar('xVal','FLIRcamera',0,dispW,nothing)
cv2.createTrackbar('yVal','FLIRcamera',0,dispH,nothing)

while True:
    ret,frame = cam.read()
    xVal = cv2.getTrackbarPos('xVal','FLIRcamera')
    yVal = cv2.getTrackbarPos('yVal','FLIRcamera')
    cv2.circle(frame,(xVal,yVal),5,(255,0,0),-1)

    
    print(xVal,yVal)
    cv2.imshow('FLIRcamera',frame)
    cv2.moveWindow('FLIRcamera',0,0)
    if cv2.waitKey(1)==ord('q'):
        break

cam.release()
cv2.destroyAllWindows()