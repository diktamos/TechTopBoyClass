from threading import Thread
import cv2
import time
import numpy as np
import face_recognition
import pickle
import sys
import os

with open('train.pkl','rb') as f:
    Names = pickle.load(f)
    Encodings = pickle.load(f)

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

W = 640
H = 480
cam1 = vStream(1,W,H)
cam2 = vStream(camSet,W,H)

font = cv2.FONT_HERSHEY_SIMPLEX
startTime = time.time()
dtav = 0
scaleFactor = .3

while True:
    try:
        myFrame1 = cam1.getFrame()
        myFrame2 = cam2.getFrame()
        myFrame3 = np.hstack((myFrame2,myFrame2))

        frameRGB = cv2.cvtColor(myFrame3,cv2.COLOR_BGR2RGB)      
        frameRGBsmall = cv2.resize(frameRGB,(0,0),fx=scaleFactor,fy=scaleFactor)

        facePositions = face_recognition.face_locations(frameRGBsmall) #model='cnn'
        allEncodings = face_recognition.face_encodings(frameRGBsmall,facePositions)
        print("for loop")

        for (top,right,bottom,left),face_encoding in zip(facePositions,allEncodings):
            name = 'Unknown Person' 
            matches = face_recognition.compare_faces(Encodings,face_encoding)
            if True in matches:
                first_match_index = matches.index(True)
                name = mane[first_match_index]
                print(name)
            
            top = int(top/scaleFactor)
            left = int(left/scaleFactor)
            right = int(right/scaleFactor)
            bottom = int(bottom/scaleFactor)

            cv2.rectangle(myFrame3,(left,top),(right,bottom),(0,0,255),2)     
            cv2.putText(myFrame3,name,(left,top+6),font,0.75,(255,0,0),2)

            print(name)


      

        dt = time.time()-startTime
        startTime = time.time()

        dtav=.95*dtav+.05*dt
        fps = str(round(1/dtav,1))+'FPS'

        #print(fps)   
        cv2.rectangle(myFrame3,(0,0),(100,40),(170,10,80),-1)      
        cv2.putText(myFrame3,fps,(0,20),font,0.65,(240,240,200),1)
        
        cv2.imshow('Combo', myFrame3)
        cv2.moveWindow('Combo',0,0)    

    except Exception as e:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        print('frame not available\n', exc_type,fname,exc_tb.tb_lineno)
        #e = sys.exc_info()[0]
        #print("<Error: %s" % e)


        #time.sleep(10)
        

    if cv2.waitKey(1)==ord('q'):
        cam1.capture.release()
        cam2.capture.release()
        cv2.destroyAllWindows()
        exit(1)
        break