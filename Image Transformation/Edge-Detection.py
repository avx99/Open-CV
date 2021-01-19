import cv2
import numpy as np

image = cv2.imread('../images/input.jpg',0)
height, width = image.shape
cv2.imshow("Original Image", image)
cv2.waitKey(0) 
sobelX = cv2.Sobel(image,cv2.CV_64F,0,1,ksize=5)
sobelY = cv2.Sobel(image,cv2.CV_64F,1,0,ksize=5)
cv2.imshow("Sobel X", sobelX) 
cv2.waitKey(0) 
cv2.imshow("Sobel Y", sobelY) 
cv2.waitKey(0) 
sobelOR = cv2.bitwise_or(sobelX,sobelY)
cv2.imshow("Sobel XorY", sobelOR) 
cv2.waitKey(0) 
lap = cv2.Laplacian(image,cv2.CV_64F)
cv2.imshow("Laplacian", lap) 
cv2.waitKey(0) 
canny = cv2.Canny(image,20,170)
cv2.imshow("Canny", canny) 
cv2.waitKey(0) 
cv2.destroyAllWindows()