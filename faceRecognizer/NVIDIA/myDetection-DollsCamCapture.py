import jetson.inference
import jetson.utils
#import cv2

#net = jetson.inference.detectNet("ssd-mobilenet-v2", threshold=0.5)
#dispW,dispH = 1280, 720
#frameRate = 21
net = jetson.inference.detectNet("ssd-mobilenet-v2",['--model=/home/jetson/Downloads/jetson-inference/python/training/detection/ssd/mytrainDollsDetectCaptureCam/ssd-mobilenet.onnx','--labels=/home/jetson/Downloads/jetson-inference/python/training/detection/ssd/mytrainDollsDetectCaptureCam/labels.txt','--input-blob=input_0','--output-cvg=scores','--output-bbox=boxes'])

camera = jetson.utils.videoSource("/dev/video1")
display = jetson.utils.videoOutput()

#outVid = cv2.VideoWriter('videos/myDetectDolls.avi',cv2.VideoWriter_fourcc(*'XVID'),frameRate,(dispW,dispH))


while True:
    img = camera.Capture()
    detections = net.Detect(img)
    
    display.Render(img)
    display.SetStatus("Object detection | Network {:.0f} FPS".format(net.GetNetworkFPS()))
    print("Object detection | Network {:.0f} FPS".format(net.GetNetworkFPS()))

   # array = jetson.utils.cudaToNumpy(img)
   # arrayCV = cv2.cvtColor(array,cv2.COLOR_RGB2BGR)
   # outVid.write(arrayCV)
    
  #  if cv2.waitKey(50)==ord('q'):
   #     break

#outVid.release()
