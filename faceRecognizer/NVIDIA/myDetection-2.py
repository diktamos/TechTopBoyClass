import jetson.inference
import jetson.utils

net = jetson.inference.detectNet("ssd-mobilenet-v2", threshold=0.5)
camera = jetson.utils.videoSource("/dev/video1")
display = jetson.utils.videoOutput()

while True:
    img = camera.Capture()
    detections = net.Detect(img)
    display.Render(img)
    display.SetStatus("Object detection | Network {:.0f} FPS".format(net.GetNetworkFPS()))

