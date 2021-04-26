import cv2
print('cv2 version:', cv2.__version__)
dispW = 640
dispH = 512
flip=2

def nothing():
    pass

cv2.namedWindow('Blended')
cv2.createTrackbar('BlendValue','Blended',50,100,nothing)


cvLogo = cv2.imread('cv.jpg')
cvLogo = cv2.resize(cvLogo,(320,256))
cvLogoGray = cv2.cvtColor(cvLogo,cv2.COLOR_BGR2GRAY)

cv2.imshow('cv Logo Gray', cvLogoGray)
cv2.moveWindow('cv Logo Gray',0, 350)

_,BGMask = cv2.threshold(cvLogoGray,225,255,cv2.THRESH_BINARY)
cv2.imshow('cv BGMask', BGMask)
cv2.moveWindow('cv BGMask',385,0)

FGMask = cv2.bitwise_not(BGMask)
cv2.imshow('FG Mask', FGMask)
cv2.moveWindow('FG Mask', 385,350)

FG = cv2.bitwise_and(cvLogo,cvLogo, mask = FGMask)
cv2.imshow('FG',FG)
cv2.moveWindow('FG',703,350)
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
while True:
    ret,frame = cam.read()
    frame = cv2.resize(frame, (320,256))

    BV1 = cv2.getTrackbarPos('BlendValue','Blended')/100
    BV2 = 1-BV1
    BG = cv2.bitwise_and(frame,frame,mask = BGMask)
    compImage = cv2.add(BG,FG)
    cv2.imshow('compImage',compImage) 
    cv2.moveWindow('compImage',1070,0)

    Blended = cv2.addWeighted(frame,BV1,cvLogo,BV2,0)
    FG2 = cv2.bitwise_and(Blended,Blended,mask = FGMask)
    
    compFinal = cv2.add(BG,FG2)
    cv2.imshow('compFinal ',compFinal ) 
    cv2.moveWindow('compFinal',1304,350)

    cv2.imshow('Blended',Blended)
    cv2.moveWindow('Blended',1017,350)

    cv2.imshow('FG2',FG2)
    cv2.moveWindow('FG2',1324,0)

    cv2.imshow('BG',BG)
    cv2.moveWindow('BG',700,0)
    cv2.imshow('FLIRcamera',frame)
    cv2.moveWindow('FLIRcamera',0,0)
    if cv2.waitKey(1)==ord('q'):
        break

cam.release()
cv2.destroyAllWindows()