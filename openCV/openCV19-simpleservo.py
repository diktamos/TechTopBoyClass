from adafruit_servokit import ServoKit
import time
myKit = ServoKit(channels=16)
while True:
    for i in range(0,90,1):
        myKit.servo[0].angle = i
        time.sleep(.01)

    for i in range(90,0,-1):
        myKit.servo[0].angle = i
        time.sleep(.01)
