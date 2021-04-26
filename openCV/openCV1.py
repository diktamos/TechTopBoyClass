import cv2
print('cv2 version:', cv2.__version__)
dispW=320
dispH=240
flip=2

camNumber = 0
#cam=cv2.VideoCapture(camSet)
cam=cv2.VideoCapture(camNumber)
while True:
    ret,frame = cam.read()
    cv2.imshow('FLIR camera',frame)
    if cv2.waitKey(1)==ord('q'):
        break

cam.release()
cv2.destroyAllWindows()


