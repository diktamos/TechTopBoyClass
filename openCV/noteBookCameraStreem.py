import cv2
import time

if __name__ == '__main__':

    camNumber = 0
    cap = cv2.VideoCapture(camNumber)

    if not cap.isOpened():
        raise IOError('We cannot open webcam')

    while(True):
        ret, frame = cap.read()
        frame_heigth = cap.get(4)
        frame_width = cap.get(3)
        print(f'h = {frame_heigth}, w = {frame_width}')
        if ret == True:
            cv2.imshow('frame', frame)
            if cv2.waitKey(25) & 0xFF == ord('q'):
                break
    
    cap.release()
   # out.releas()
    cv2.destroyAllWindows()
