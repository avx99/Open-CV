import cv2
import numpy as np


#store image in a var
v = cv2.imread('../images/input.jpg')

#plot the image
cv2.imshow('first image :D',v)

#to wait
cv2.waitKey()

#close windows
cv2.destroyAllWindows()

#to save image we use this(x its v -10)
x = v - 10
cv2.imwrite('output.jpg',x)