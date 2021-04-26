import cv2
print('cv2 version:', cv2.__version__)
dispW = 640 #640
dispH = 480 #512
flip=0

#for rasbery pi camera

camSet='nvarguscamerasrc !  video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=21/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(dispW)+', height='+str(dispH)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'

#camNumber = 0
cam=cv2.VideoCapture(camSet)
face_cascade = cv2.CascadeClassifier('/home/jetson/Desktop/pyPro/cascades/face.xml')
eye_cascade = cv2.CascadeClassifier('/home/jetson/Desktop/pyPro/cascades/eye.xml')
#cam = cv2.VideoCapture(camNumber)
while True:
    ret,frame = cam.read()
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray,1.3,5)
    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),2)
        roi_gray = gray[y:y+h,x:x+w]
        roi_color = frame[y:y+h,x:x+w]
        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (xEye,yEye,wEye,hEye) in eyes:
            cv2.rectangle(roi_color,(xEye,yEye),(xEye+wEye,yEye+hEye),(255,0,0),2) 
            #cv2.circle(roi_color,(int(xEye+wEye/2),int(yEye+hEye/2)),int(wEye/2),(255,0,0),-1) 
   # print('ret: ',ret)
    cv2.imshow('Rassbery camera',frame)
    cv2.moveWindow('Rassbery camera',0,0)
    if cv2.waitKey(1)==ord('q'):
        break

cam.release()
cv2.destroyAllWindows()