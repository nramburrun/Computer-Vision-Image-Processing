import cv2
import numpy as np 

img = cv2.imread('test-images/bookpage.jpg')
retval, threshold = cv2.threshold(img,12,255,cv2.THRESH_BINARY)

grayscaled = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
retval2, threshold2 = cv2.threshold(grayscaled,12,255, cv2.THRESH_BINARY)

#gaussian adaptive threshold 
#TO DO: explain what it does and see whats going on
gaus = cv2.adaptiveThreshold(grayscaled, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 1)

cv2.imshow('og', img)
cv2.imshow('threshold', threshold)
cv2.imshow('grayscaled', threshold2)
cv2.imshow('gaussian', gaus)
print(retval)
print(retval2)
cv2.waitKey(0)
cv2.destroyAllWindows()