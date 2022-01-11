import cv2 as cv
import numpy as np

blank_photo = np.zeros((600,650,3), dtype='uint8')
blank_photo[:] = 0,0,0

#Rectangle
cv.rectangle(blank_photo, (0,0), (250,250), (0,255,0), thickness=1)

# Circle
cv.circle(blank_photo, (250,250),40,(0,0,255), thickness=-1)


#Line
cv.line(blank_photo, (0,0), (500,250), (0,255,0), thickness=3)

#Writing text 
cv.putText(blank_photo,'Morvin Black', (255,255), cv.FONT_HERSHEY_COMPLEX_SMALL, 1.0, (255,255,255),2)

cv.imshow("Photo",blank_photo)

cv.waitKey(0)