#Playong a video
import cv2
import numpy as np


capture = cv2.VideoCapture(0)

#Resize
def rescale(frame, scale=0.65):
    width = int(frame.shape[1]*scale)
    height = int(frame.shape[0]*scale)

    dimension = (width, height)
    return cv2.resize(frame,dimension,interpolation=cv2.INTER_AREA)
    

while (True):
    ret, frame = capture.read()
    resized_frame = rescale(frame)
    gray = cv2.cvtColor(resized_frame,cv2.COLOR_BGR2GRAY)
 
    cv2.imshow('video',frame)
    cv2.imshow('Video resized', gray)


    if cv2.waitKey(20) & 0xFF == ord('q'):
        break


capture.release()
cv2.destroyAllWindows()
