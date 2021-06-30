import jetson.inference
import jetson.utils


#cam = jetson.utils.gstCamera(640,512,"/dev/video1")
cam = jetson.utils.gstCamera(0)
disp = jetson.utils.glDisplay()
font = jetson.utils.cudaFont()

while disp.IsOpen():
    frame, width, height = cam.CaptureRGBA()
    

    font.OverlayText(frame,width,height,'item',5,5,font.Magenta,font.Blue)
    disp.RenderOnce(frame,width,height)
