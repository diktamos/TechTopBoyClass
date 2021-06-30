import jetson.inference
import jetson.utils
import time
import cv2
import numpy as np


width = 1280
height = 720

#cam = jetson.utils.gstCamera(width,height,1)
cam = jetson.utils.gstCamera(0)


net = jetson.inference.imageNet('googlenet')

font = cv2.FONT_ITALIC

timeMark = time.time()
fpsFilter = 0

while True:
    frame, width, height = cam.CaptureRGBA(zeroCopy=1)
    
    classID, confidence = net.Classify(frame,width,height)
    item = net.GetClassDesc(classID)
    dt = time.time() -timeMark
    fps = 1/dt
    fpsFilter = 0.95*fpsFilter+0.05*fps
    fpsFilterStr = str(round(fpsFilter,1))+' fps; '
    timeMark = time.time()
    #font.OverlayText(frame,width,height,fpsFilterStr+item,5,5,font.Magenta,font.Blue)
    #display.RenderOnce(frame,width,height)
    frame=jetson.utils.cudaToNumpy(frame,width,height,4)
    frame = cv2.cvtColor(frame,cv2.COLOR_RGBA2BGR).astype(np.uint8)

    cv2.putText(frame,fpsFilterStr+item,(0,30),font,1,(0,0,255),2)
    cv2.imshow('recCam',frame)
    cv2.moveWindow('recCam',0,0)

    if cv2.waitKey(1)==ord('q'):
        break

cam.release()
cv2.destroyAllWindows()


