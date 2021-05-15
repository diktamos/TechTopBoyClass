import face_recognition
import cv2
print(cv2.__version__)

image = face_recognition.load_image_file('/home/jetson/Desktop/pyPro/faceRecognizer/demoImages/unknown/u3.jpg')
face_locations = face_recognition.face_locations(image)
print(face_locations) 
image = cv2.cvtColor(image,cv2.COLOR_RGB2BGR)
for (r1,c1,r2,c2) in face_locations:
    cv2.rectangle(image,(c1,r1),(c2,r2),(100,0,255),2)
cv2.imshow('myWindow',image)
cv2.moveWindow('myWindow',0,0)
if cv2.waitKey(0)==ord('q'):
    cv2.destroyAllWindows()
    