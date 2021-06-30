import jetson.inference
import jetson.utils
import time

net = jetson.inference.imageNet('googlenet')
#cam = jetson.utils.gstCamera(640,512,"/dev/video1")
cam = jetson.utils.gstCamera(0)
disp = jetson.utils.glDisplay()
font = jetson.utils.cudaFont()

while disp.IsOpen():
    frame, width, height = cam.CaptureRGBA()
    item = 'bu'
    
    classID, confident = net.Classify(frame,width,height)
    
    print("classID",classID)
    if classID:
        item = net.GetClassDesc(classID)
    


    font.OverlayText(frame,width,height,item,5,5,font.Magenta,font.Blue)
    disp.RenderOnce(frame,width,height)

