from threading import Thread
import time
def BigBox(color,l):
    while True:
        print(color,'Big Box is Open of length',l)
        time.sleep(5)
        print(color,'Big Box is Closed of length',l)
        time.sleep(5)

def SmallBox(color,l):
    while True:
        print(color,'Small Box is Open of length',l)
        time.sleep(1)
        print(color,'Small Box is Closed of length',l)
        time.sleep(1)


l1 = 6
l2 = 8

bigBoxThread = Thread(target=BigBox,args=('red',l1))
smallBoxThread = Thread(target=SmallBox,args=('blue',l2))

bigBoxThread.daemon = True
smallBoxThread.daemon = True

bigBoxThread.start()
smallBoxThread.start()

while True:
    pass