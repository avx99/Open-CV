import cv2
import numpy as np

v = cv2.imread('../images/input.jpg')
cv2.imshow('original',v)
cv2.waitKey()

B,G,R =  cv2.split(v)
cv2.imshow('Blue',B)
cv2.waitKey()
cv2.imshow('Green',G)
cv2.waitKey()
cv2.imshow('Red',R)
cv2.waitKey()
cv2.destroyAllWindows()

#merge images
merged = cv2.merge([B,G,R])
cv2.imshow('Merged',merged)
cv2.waitKey()
cv2.destroyAllWindows()

#rgb
zeros = np.zeros(v.shape[:2],dtype='uint8')
cv2.imshow('Blue',cv2.merge([B,zeros,zeros]))
cv2.waitKey()
cv2.imshow('Green',cv2.merge([zeros,G,zeros]))
cv2.waitKey()
cv2.imshow('Red',cv2.merge([zeros,zeros,R]))
cv2.waitKey()
cv2.destroyAllWindows()