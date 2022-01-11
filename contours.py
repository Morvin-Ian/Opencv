import cv2 as cv
import numpy as np

Image = cv.imread('Pictures/firmino.jpg')
# cv.imshow("Firmino",Image)

blank_photo = np.zeros((700,600),dtype='uint8')


Blur = cv.GaussianBlur(Image,(3,3), cv.BORDER_DEFAULT)
# cv.imshow("Blur Firmino",Blur)


Edge = cv.Canny(Blur,125,175)
cv.imshow("Canny", Edge)

ret,thresh = cv.threshold(Image, 100, 250,cv.THRESH_BINARY)
cv.imshow("Threshhold", thresh)


contours, hierachies = cv.findContours(Edge,cv.RETR_LIST,cv.CHAIN_APPROX_NONE)
print(len(contours))

cv.drawContours(blank_photo,contours,-1,(255,0,6),2)
cv.imshow("Blank Contour",blank_photo)
cv.waitKey(0)

