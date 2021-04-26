import cv2
import random
print('cv2 version:', cv2.__version__)

class Ball():
    def __init__(self,xCenter=100,yCenter=100, radius=10, color = [255,0,255], lineWidth = -1, dt = 0.01):
        self.xCenter = xCenter
        self.yCenter = yCenter
        self.radius = radius
        self.color = color
        self.lineWidth = lineWidth
        self.dt = dt
        self.time = 0-dt
        self.vx = 1 #random.randint(-1,1)
        self.vy = 1 #random.randint(-1,1)


    def Draw(self,frame):
        self.time += self.dt
        self.xCenter = int(self.xCenter + self.time * self.vx)
        self.yCenter = int(self.yCenter + self.time * self.vy)

        if self.xCenter >= 640 or self.xCenter <= 0:
            self.vx = -self.vx
        if self.yCenter >=512 or self.yCenter <=0:
            self.vy = -self.vy



        return cv2.circle(frame,(self.xCenter,self.yCenter),self.radius,self.color, self.lineWidth)


   

dispW=320
dispH=240
flip=2
frameNumber = 0
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
cam=cv2.VideoCapture(camNumber)
ball = Ball()
while True:
    ret,frame = cam.read()
    frame = cv2.rectangle(frame,(140,100),(180,340),(255,255,0),4)
    frame = cv2.circle(frame,(400,120),50,(255,0,255),-1)
    fnt = cv2.FONT_HERSHEY_DUPLEX
    frame = cv2.putText(frame,'My First Text '+ str(frameNumber),(300,300),fnt,1,(255,0,150),2) # font,size,color,thikness
    frame = cv2.line(frame,(10,10),(500,400),(0,0,0),3)
    frame = cv2.arrowedLine(frame,(10,470),(300,470),(255,255,255),3)

    frame = ball.Draw(frame)


    cv2.imshow('FLIRcamera',frame)
    cv2.moveWindow('FLIRcamera',0,0)
    frameNumber += 1
    if cv2.waitKey(1)==ord('q'):
        break

cam.release()
cv2.destroyAllWindows()