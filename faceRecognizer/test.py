import face_recognition
import cv2
import os
import pickle

print(cv2.__version__)

Encodings = []
Names = []

#image_dir ='/home/jetson/Desktop/pyPro/faceRecognizer/demoImages/known'
image_dir ='/home/jetson/Desktop/pyPro/faceRecognizer/demoImages/Data'

for root, dirs, files in os.walk(image_dir):
    print(files)
    for file in files:
        path = os.path.join(root,file) 
        print(path)
        name = os.path.splitext(file)[0]
        print(name)
        person = face_recognition.load_image_file(path)
        print(name,' ',type(person), person.size,person.shape)
        
        coefW = 480/(min(person.shape[0],person.shape[1]))
        coefW = round(coefW,1)
        print(coefW, round(coefW,1))
        person = cv2.resize(person,None,fx=coefW, fy=coefW)
        personGBR = cv2.cvtColor(person,cv2.COLOR_RGB2BGR)
        
        cv2.imshow('person',personGBR)
        cv2.moveWindow('person',0,0)
        
        encoding = face_recognition.face_encodings(person)
        if len(encoding) == 0:
            person = cv2.rotate(person, cv2.ROTATE_90_COUNTERCLOCKWISE)
            cv2.imshow('person',person)
            cv2.moveWindow('person',600,0)

        print('person resized:', person.size)
        if cv2.waitKey(0)==ord('q'):
            cv2.destroyAllWindows()
        
           


               
        
     
