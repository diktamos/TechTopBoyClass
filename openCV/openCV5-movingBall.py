import cv2
import random
import matplotlib.pyplot as plt
print('cv2 version:', cv2.__version__)

class Ball():
    def __init__(self,xCenter=100,yCenter=100, radius=10, color = [255,0,255], lineWidth = -1, dt = 1):
        self.xCenter = xCenter
        self.yCenter = yCenter
        self.radius = radius
        self.color = color
        self.lineWidth = lineWidth
        self.dt = dt
        self.time = 0-dt
        self.vx = 0.05 #random.randint(-1,1)
        self.vy = 0.05 #random.randint(-1,1)


    def Draw(self,frame):
        self.time += self.dt
        self.xCenter = int(self.xCenter + self.time * self.vx)
        self.yCenter = int(self.yCenter + self.time * self.vy)

        if self.xCenter >= 640 or self.xCenter <= 0:
            self.vx = -self.vx
        if self.yCenter >=512 or self.yCenter <=0:
            self.vy = -self.vy



        return cv2.circle(frame,(self.xCenter,self.yCenter),self.radius,self.color, self.lineWidth)


   

dispW=640
dispH=512

frameNumber = 0

camNumber = 0
#cam=cv2.VideoCapture(camSet)
cam=cv2.VideoCapture(camNumber)
ball = Ball()

while True:
    ret,frame = cam.read()
    
    fnt = cv2.FONT_HERSHEY_DUPLEX
    
    frame = cv2.putText(frame,'Frame number'+ str(frameNumber),(300,300),fnt,1,(255,0,150),2) # font,size,color,thikness
    frame = cv2.putText(frame,'vx = '+ str(ball.vx),(300,320),fnt,1,(255,0,150),2) # font,size,color,thikness
    frame = cv2.putText(frame,'vy = '+ str(ball.vy),(300,340),fnt,1,(255,0,150),2) # font,size,color,thikness

    frame = ball.Draw(frame)
    cv2.imshow('FLIRcamera',frame)
    cv2.moveWindow('FLIRcamera',0,0)
    plt.plot(ball.vx,'r*',label='vx')
    plt.plot(ball.vy,'b*',label='vy')
    plt.legend()
   
    
    frameNumber += 1
    if cv2.waitKey(5)==ord('q'):
        break
plt.show()
cam.release()
cv2.destroyAllWindows()