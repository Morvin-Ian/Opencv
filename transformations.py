import cv2 as cv
import numpy as np

image = cv.imread('opencv/Pictures/12.jpg')
def rescale(frame, scale=0.35):
    width = int(frame.shape[1]*scale)
    height = int(frame.shape[0]*scale)

    dimension = (width, height)
    return cv.resize(frame,dimension,interpolation=cv.INTER_AREA)
    
resized = rescale(image)

#Translation
def translate(resized, x,y):
    trans = np.float32([[1,0,x],[0,1,y]])
    dimensions = (resized.shape[1], resized.shape[0])
    return cv.warpAffine(resized,trans,dimensions)

#Roration
def rotation(resized, angle, rotPoint=None):
    (height,width) = resized.shape[:2]
    if rotPoint is None:
        rotPoint = (width//2, height//2)
        rotImage =cv.getRotationMatrix2D(rotPoint,angle,1.0)
        dimemsions = (width, height)
        return cv.warpAffine(resized,rotImage,dimemsions)

#flipping
flip=cv.flip(resized,1)
cv.imshow("Flipped", flip)
cv.imshow("Flipped_Confirm", resized)


rotated = rotation(resized, 90)
cv.imshow("Rotated", rotated)
   
translated = translate(resized,-50,100)
cv.imshow("Translated", translated)
cv.waitKey(0)