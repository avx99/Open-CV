import cv2
import numpy as np

v = cv2.imread('../images/input.jpg')
cv2.imshow('original',v)
cv2.waitKey()

grayImg =  cv2.cvtColor(v,cv2.COLOR_BGR2GRAY)
cv2.imshow('gray',grayImg)
cv2.waitKey()
cv2.destroyAllWindows()
