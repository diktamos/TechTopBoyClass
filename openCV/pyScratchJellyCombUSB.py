import cv2
print('cv2 version:', cv2.__version__)
dispW = 640
dispH = 512
flip=2
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
    h,w,_ = frame.shape[:]
    print(type(h))
    w=int(w/2)
    h=int(h/2)
    frame =cv2.resize(frame,(w,h))
   

    cv2.imshow('JellyCombUSB',frame)
    cv2.moveWindow('JellyCombUSB',0,0)
    if cv2.waitKey(1)==ord('q'):
        break

cam.release()
cv2.destroyAllWindows()