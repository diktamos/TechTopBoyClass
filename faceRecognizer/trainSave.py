import face_recognition
import cv2
import os
import pickle

print(cv2.__version__)

Encodings = []
Names = []

image_dir ='/home/jetson/Desktop/pyPro/faceRecognizer/demoImages/known'


for root, dirs, files in os.walk(image_dir):
    print(files)
    for file in files:
        path = os.path.join(root,file) 
        print(path)
        name = os.path.splitext(file)[0]
        print(name)
        person = face_recognition.load_image_file(path)
        print(name,' ',len(person))
        person = cv2.resize(person,None,fx=0.3, fy=0.3, interpolation = cv2.INTER_CUBIC)
        print('person resized:', len(person))
        encoding = face_recognition.face_encodings(person)[0]
        
        Encodings.append(encoding)
        Names.append(name)
print(Names)

with open('train.pkl','wb') as f:
    pickle.dump(Names,f)
    pickle.dump(Encodings,f)
