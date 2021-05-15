import cv2
print('cv2 version:', cv2.__version__)
dispW = 640
dispH = 512
flip=2
posY = 10
posX = 10
BW = 30
BH = 30
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
camNumber = 1
#cam=cv2.VideoCapture(camSet)
cam = cv2.VideoCapture(camNumber)

while True:
    ret,frame = cam.read()
    roi = frame[posY:posY+BH,posX:posX+BW].copy()

    frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    frame = cv2.cvtColor(frame,cv2.COLOR_GRAY2BGR)

  
    frame[posY:posY+BH,posX:posX+BW]= roi
    cv2.rectangle(frame,(posX,posY),(posX+BW,posY+BH),[255,0,0],2)

    cv2.imshow('ROI',roi)

    cv2.imshow('FLIRcamera',frame)
    cv2.moveWindow('FLIRcamera',0,0)
    if cv2.waitKey(1)==ord('q'):
        break

cam.release()
cv2.destroyAllWindows()