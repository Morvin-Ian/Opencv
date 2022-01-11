import cv2 as cv
import numpy as np

img = cv.imread('Pictures/12.jpg',)
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Image',gray)

key = cv.waitKey(0)
if key == ord('q'):
    cv.destroyAllWindows()
elif key == ord('s'):
    cv.imwrite('Cinatown.jpg', gray)
    cv.destroyAllWindows()