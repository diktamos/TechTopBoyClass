from threading import Thread
import cv2
import time
import numpy as np

class vStream:
    def __init__(self,src,width,height):
        self.width = width
        self.height = height
        self.capture = cv2.VideoCapture(src)
        self.thread = Thread(target=self.update)
        self.thread.daemon=True
        self.thread.start()

    def update(self):
        while True:
            _,self.frame = self.capture.read()
            self.frame2 = cv2.resize(self.frame,(self.width,self.height))

    def getFrame(self):
        return self.frame2
        

flip = 0
dispW = 640
dispH = 480
camSet='nvarguscamerasrc !  video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=21/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(dispW)+', height='+str(dispH)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'

W = 320
H = 240
cam1 = vStream(1,W,H)
cam2 = vStream(camSet,W,H)

font = cv2.FONT_HERSHEY_SIMPLEX
startTime = time.time()
dtav = 0
while True:
    try:
        myFrame1 = cam1.getFrame()
        myFrame2 = cam2.getFrame()
        myFrame3 = np.hstack((myFrame1,myFrame2))
        
      

        dt = time.time()-startTime
        startTime = time.time()

        dtav=.95*dtav+.05*dt
        fps = str(round(1/dtav,1))+'FPS'

        #print(fps)   
        cv2.rectangle(myFrame3,(0,0),(100,40),(170,10,80),-1)      
        cv2.putText(myFrame3,fps,(0,20),font,0.65,(240,240,200),1)
        
        cv2.imshow('Combo', myFrame3)
        cv2.moveWindow('Combo',0,0)    

    except:
        print('frame not available')
       # time.sleep(10)
        

    if cv2.waitKey(1)==ord('q'):
        cam1.capture.release()
        cam2.capture.release()
        cv2.destroyAllWindows()
        exit(1)
        break