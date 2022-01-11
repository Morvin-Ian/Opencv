import cv2 as cv
import numpy as np

img = cv.imread('opencv/Pictures/12.jpg',-1)
# cv.imshow('Laptop',img)


def rescale(frame, scale=0.35):
    width = int(frame.shape[1]*scale)
    height = int(frame.shape[0]*scale)

    dimension = (width, height)
    return cv.resize(frame,dimension,interpolation=cv.INTER_AREA)
    
resized = rescale(img)
cv.imshow('Resized Image', resized)

#Convert to grayscale
gray = cv.cvtColor(resized,cv.COLOR_BGR2GRAY)
cv.imshow("Grayscale", gray)

# Blur the image
blur = cv.GaussianBlur(resized,(3,3), cv.BORDER_DEFAULT)
cv.imshow("Blured", blur)

#Edge cascade
edge = cv.Canny(blur,125,175)
cv.imshow("Canny", edge)

#Dialating an image
dialated = cv.dilate(edge, (9,9), iterations=4)
cv.imshow("Dialated", dialated)

#resize
res = cv.resize(gray, (500,300), interpolation=cv.INTER_CUBIC)
cv.imshow("Resized",res)

#Crop
cropped = img[50:200,100:300]
cv.imshow("Cropped",cropped)
cv.waitKey(0)