import cv2
print('cv2 version:', cv2.__version__)
dispW = 1280 #640 #640
dispH = 720 #480 #512
flip=0

#for rasbery pi camera

camSet='nvarguscamerasrc sensor-id=0 wbmode=daylight tnr-mode=1 tnr-strength=1 ee-mode=2 ee-strength=1 !  video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=21/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(dispW)+', height='+str(dispH)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! videobalance contrast=1.5 brightness=-.15 saturation=1.2 ! appsink'

#camNumber = 0
cam=cv2.VideoCapture(camSet)

#cam = cv2.VideoCapture(camNumber)
while True:
    ret,frame = cam.read()
    
    cv2.imshow('Rassbery camera',frame)
    cv2.moveWindow('Rassbery camera',0,0)
    if cv2.waitKey(1)==ord('q'):
        break

cam.release()
cv2.destroyAllWindows()