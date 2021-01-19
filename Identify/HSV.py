import cv2
import numpy as np

v = cv2.imread('../images/input.jpg')
cv2.imshow('original',v)
cv2.waitKey()

HSVImg =  cv2.cvtColor(v,cv2.COLOR_BGR2HSV)
cv2.imshow('HSV',HSVImg)
cv2.waitKey()
cv2.imshow('Hue',HSVImg[:,:,0])
cv2.waitKey()
cv2.imshow('Saturation',HSVImg[:,:,1])
cv2.waitKey()
cv2.imshow('Value',HSVImg[:,:,2])
cv2.waitKey()
cv2.destroyAllWindows()

