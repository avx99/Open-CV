import cv2
import numpy as np

image = cv2.imread('../images/opencv_inv.png')
cv2.imshow('Original', image)
cv2.waitKey()
kernel = np.ones((5,5),np.uint8)
ero = cv2.erode(image,kernel,iterations=1)
cv2.imshow('Erosion', ero)
cv2.waitKey()
dil = cv2.dilate(image,kernel,iterations=1)
cv2.imshow('Dilation', dil)
cv2.waitKey()
cv2.destroyAllWindows()