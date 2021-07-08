import cv2
import time

print('cv2 version:', cv2.__version__)
dispW = 1920
dispH = 1080
flip=2
frameRate = 0

class Rechteck():
    def __init__(self,xCenter0=100,yCenter0=100, radius=50, color = [255,0,255], lineWidth = -1, dt = 1,dispW=1920,dispH=1080):
        self.xCenter0 = xCenter0
        self.yCenter0 = yCenter0
        self.xCenter = xCenter0
        self.yCenter = yCenter0
        self.radius = radius
        self.color = color
        self.lineWidth = lineWidth
        self.dt = dt
        self.time = 0-dt
        self.vx = 20 #random.randint(-1,1)
        self.vy = 20 #random.randint(-1,1)
        self.dispW = dispW
        self.dispH = dispH


    def Move(self):
       # self.time += self.dt
        self.xCenter = int(self.xCenter + self.dt * self.vx)
        self.yCenter = int(self.yCenter + self.dt * self.vy)

        if self.xCenter+self.radius >= int(self.dispW):
            self.vx = -self.vx
            self.xCenter = int(self.dispW) -self.radius 
            
            
        if self.xCenter <= 0:
            self.vx = -self.vx
            self.xCenter = 0
           
        if self.yCenter+self.radius >= int(self.dispH):
            self.vy = -self.vy
            self.yCenter = int(self.dispH) - self.radius 
           
            
        if self.yCenter <=0:
            self.vy = -self.vy
            self.yCenter = 0
           
            

            
 

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
logoBox = Rechteck(dispH=dispH,dispW=dispW)
logo = cv2.imread('pl.jpg')
logo = cv2.resize(logo, (50,50))
cv2.imshow('logo',logo)
cv2.moveWindow('logo',720,0)

logoGray = cv2.cvtColor(logo, cv2.COLOR_BGR2GRAY)
_,logoMask = cv2.threshold(logoGray,225,255,cv2.THRESH_BINARY)

cv2.imshow('logoMask',logoMask)
cv2.moveWindow('logoMask', 780,0)

FGMask = cv2.bitwise_not(logoMask )
cv2.imshow('FG Mask', FGMask)
cv2.moveWindow('FG Mask', 780,120)

FG = cv2.bitwise_and(logo,logo,mask=FGMask)
cv2.imshow('FG ', FG)
cv2.moveWindow('FG ', 780,240)

camNumber = 1
#cam=cv2.VideoCapture(camSet)
cam = cv2.VideoCapture(camNumber)
start = time.time()
while True:
    ret,frame = cam.read()
    print(frame.shape)
    
    roiBox = frame[logoBox.yCenter:logoBox.yCenter+logoBox.radius,\
            logoBox.xCenter:logoBox.xCenter+logoBox.radius].copy()
    cv2.imshow('roiBox',roiBox)
    cv2.moveWindow('roiBox',840,0)

    BG = cv2.bitwise_and(roiBox,roiBox,mask = logoMask)
    cv2.imshow('BG ',BG )
    cv2.moveWindow('BG ',900,0)

    #roiComb = cv2.addWeighted(FG,0.5,BG,0.5,0)
    roiComb = cv2.add(FG,BG)
    cv2.imshow('roiComb ',roiComb  )
    cv2.moveWindow('roiComb ',960,0)

    frame[logoBox.yCenter:logoBox.yCenter+logoBox.radius,\
            logoBox.xCenter:logoBox.xCenter+logoBox.radius] = roiComb 


 
    cv2.imshow('FLIRcamera',frame)
    cv2.moveWindow('FLIRcamera',0,0)
    frameRate += 1
    logoBox.Move()
    if time.time() - start > 1:
        print('frame per secon: ', frameRate)
        frameRate = 0
        start = time.time() 
    if cv2.waitKey(1)==ord('q'):
        break

cam.release()
cv2.destroyAllWindows()