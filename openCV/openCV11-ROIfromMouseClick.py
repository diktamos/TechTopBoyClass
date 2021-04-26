import cv2
print('cv2 version:', cv2.__version__)
dispW = 640
dispH = 512
flip=2
goFlag = 0

def mouse_click(event,x,y,fralgs,params):
        global x1,y1,x2,y2,goFlag
        if event==cv2.EVENT_LBUTTONDOWN:
                x1, y1 = x, y
                goFlag = 0
        if event==cv2.EVENT_LBUTTONUP:
                x2, y2 = x, y
                goFlag = 1



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
cv2.namedWindow('FLIRcamera')
cv2.setMouseCallback('FLIRcamera',mouse_click)
while True:
    ret,frame = cam.read()
    if goFlag == 1:
            frame = cv2.rectangle(frame, (x1,y1),(x2,y2),(255,0,0),3)
            rio = frame[y1:y2,x1:x2].copy()
            cv2.imshow('click',rio)
            cv2.moveWindow('click',712,0)
    cv2.imshow('FLIRcamera',frame)
    cv2.moveWindow('FLIRcamera',0,0)
    if cv2.waitKey(1)==ord('q'):
        break

cam.release()
cv2.destroyAllWindows()