import cv2
print('cv2 version:', cv2.__version__)
dispW = 640
dispH = 512
flip=2
frameRate = 21
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
camNumber = 100 #100 - file

if camNumber == 100:
        cam = cv2.VideoCapture('videos/myCam.avi')
        outVid = cv2.VideoWriter('videos/myCam2.avi',cv2.VideoWriter_fourcc(*'XVID'),frameRate,(dispW,dispH))
elif camNumber == 0:
        cam = cv2.VideoCapture(camNumber)
        outVid = cv2.VideoWriter('videos/myCam.avi',cv2.VideoWriter_fourcc(*'XVID'),frameRate,(dispW,dispH))

while True:
    ret,frame = cam.read()
    cv2.imshow('FLIRcamera',frame)
    cv2.moveWindow('FLIRcamera',0,0)
    outVid.write(frame)
    if cv2.waitKey(50)==ord('q'):
        break

cam.release()
outVid.release()
cv2.destroyAllWindows()