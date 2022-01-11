import cv2 as cv
import numpy as np

capture = cv.VideoCapture(0)
fourcc = cv.VideoWriter_fourcc(*"MJPG")
out = cv.VideoWriter("output.avi",fourcc, 20.0,(560,500))

while (True):
    ret, frame = capture.read()
    out.write(frame)
    cv.imshow("Recorded",frame)
  

    if cv.waitKey(20) & 0xFF == ord('q'):
        break


capture.release()
out.release()
cv.destroyAllWindows()
