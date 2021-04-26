import cv2
import numpy as np
print('cv2 version:', cv2.__version__)
evt = -1
coord = []
dispW = 640
dispH = 512
img = np.zeros((250,250,3),np.uint8)
def click(event,x,y,flags,params):
    global pnt
    global evt
    if event==cv2.EVENT_LBUTTONDOWN:
        print('Mouse Event was: ', event)
        print(x,',',y)
        pnt = (x,y)
        coord.append(pnt)
        print(coord)
        evt = (event)
    elif event==cv2.EVENT_RBUTTONDOWN:
        print(x,y) 
        blue = int(frame[y,x,0])
        green = int(frame[y,x,1])
        red = int(frame[y,x,2])
        colorString = str(blue)+','+str(green)+','+str(red)
        img[:] = [blue,green,red]
        font = cv2.FONT_HERSHEY_PLAIN
        #(r,g,b) = 255-red, 255-green, 255-blue
        tp = (255-red, 255-green, 255-blue)
        cv2.putText(img,colorString,(10,25),font,1,tp,2)
        cv2.imshow('myColor',img)
       #print(blue,green,red)
        




cv2.namedWindow('FLIRcamera')
cv2.setMouseCallback('FLIRcamera',click)

camNumber = 0
#cam=cv2.VideoCapture(camSet)
cam = cv2.VideoCapture(camNumber)
while True:
    ret,frame = cam.read()
   
    if evt==1:
        for pnts in coord:
            cv2.circle(frame,pnts,5,(0,0,255),-1)
            font = cv2.FONT_HERSHEY_PLAIN
            cv2.putText(frame,str(pnts),pnts,font,1.5,(255,0,0),2)
            

    cv2.imshow('FLIRcamera',frame)
    cv2.moveWindow('FLIRcamera',0,0)
    keyEvent = cv2.waitKey(1)
    if keyEvent==ord('q'):
        break
    elif keyEvent==ord('c'):
        coord = []

cam.release()
cv2.destroyAllWindows()