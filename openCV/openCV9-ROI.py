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
camNumber = 0
#cam=cv2.VideoCapture(camSet)
cam = cv2.VideoCapture(camNumber)
BW = (.2*dispW)
BH = (.2*dispH)
dy =2 
while True:
    ret,frame = cam.read()
    roi = frame[50:250,200:400].copy()

    roiGray = cv2.cvtColor(roi,cv2.COLOR_BGR2GRAY)
    roiGray = cv2.cvtColor(roiGray,cv2.COLOR_GRAY2BGR)
    #frame[50:250,200:400] = [255,255,255]
    #print('frame object', type(frame))
    #print('frame[50,200]: ',frame[50,200])
    #print('roiGray[0,0]: ',roiGray[0,0])
    #roiGray[:,:][0] = roiGray[:,:][0]
    
    frame[50:250,200:400]= roiGray
    cv2.imshow('ROI',roi)
   # print(roi[0,0][0])
   # print(roi[0,0][1])
   # print(roi[0,0][2])
    cv2.imshow('FLIRcamera',frame)
    cv2.imshow('GRAY',roiGray)
    cv2.moveWindow('GRAY',705,250)
    cv2.moveWindow('ROI',705,0)
    cv2.moveWindow('FLIRcamera',0,0)
    if cv2.waitKey(1)==ord('q'):
        break

cam.release()
cv2.destroyAllWindows()