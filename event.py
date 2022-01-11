import cv2 as cv
import numpy as np

def draw_circle(event,x,y,flags,param):
    if event == cv.EVENT_LBUTTONDBLCLK:
        cv.circle(blank_photo, (250,250),40,(0,0,255), thickness=-1)


blank_photo = np.zeros((600,550,3), dtype='uint8')
cv.namedWindow('Image')
cv.setMouseCallback('Image',draw_circle)

cv.imshow("Circle drawer",blank_photo)
cv.waitKey(0)