import face_recognition
import cv2
import os
import pickle
dispW = 640 #640
dispH = 480 #512
flip=0

print(cv2.__version__)

Encodings = []
Names = []

with open('/home/jetson/Desktop/pyPro/train.pkl','rb') as f:
    Names = pickle.load(f)
    Encodings = pickle.load(f)

camSet='nvarguscamerasrc !  video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=21/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(dispW)+', height='+str(dispH)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'
cam=cv2.VideoCapture(camSet)
font = cv2.FONT_HERSHEY_SIMPLEX
while True:
    _,frame = cam.read()
    frameSmall = cv2.resize(frame,(0,0),fx=0.33,fy=0.33)
    frameRGB = cv2.cvtColor(frameSmall,cv2.COLOR_BGR2RGB)
    facePositions = face_recognition.face_locations(frameRGB)#,model='cnn')
    allEncodings = face_recognition.face_encodings(frameRGB,facePositions)
    for (top,right,bottom,left),face_encodings in zip(facePositions,allEncodings):
        name = "Unknown Person"
        matches = face_recognition.compare_faces(Encodings,face_encodings)
        if True in matches:
            first_match_index = matches.index(True)
            name = Names[first_match_index]
        top = top*3
        right = right*3
        bottom = bottom*3
        left = left*3
        cv2.rectangle(frame,(left,top),(right, bottom),(0,100,255),2)
        cv2.putText(frame,name,(left,top-6),font,.75,(100,0,255))
    
    cv2.imshow('Picture',frame)
    cv2.moveWindow('Picture',0,0)
    if cv2.waitKey(1)==ord('q'):
        break
cam.release()
cv2.destroyAllWindows()



