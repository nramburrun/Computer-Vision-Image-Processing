import cv2
import numpy as np 

img1 = cv2.imread('test1.jpg')
img2 = cv2.imread('test2.jpg')

#add = img1 + img2
#add = cv2.add(img1,img2)
#weighted = cv2.addWeighted(img1, 0.6, img2, 0.4, 0)

rows,cols,channels = img2.shape
region = img1[0:rows,0:cols]

img2gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
ret, mask = cv2.threshold(img2gray, 220, 255, cv2.THRESH_BINARY_INV) #anything above 220 is converted to 255. anything less is converted to 0 but flipped

mask_inv = cv2.bitwise_not(mask)

img1_bg = cv2.bitwise_and(region,region,mask=mask_inv)
img2_fg = cv2.bitwise_and(img2,img2, mask=mask)


dst = cv2.add(img1_bg, img2_fg)
img1[0:rows,0:cols] = dst


cv2.imshow('img2gray', img2gray)
cv2.imshow('mask', mask)
cv2.imshow('mask_inv', mask_inv)
cv2.imshow('img1_bg', img1_bg)
cv2.imshow('img2_fg', img2_fg)

cv2.imshow('res', img1)
cv2.waitKey(0)
cv2.destroyAllWindows()