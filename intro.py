import cv2
import numpy as np 
import matplotlib.pyplot as plt 

img = cv2.imread('test-images/test1.jpg',cv2.IMREAD_GRAYSCALE) #convert to grayscale to deal with one color only

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

#plt.imshow(img, cmap='gray',interpolation='bicubic') #show stuff
#plt.plot([50,100],[80,100], 'c', linewidth = 5) #plot stuff
#plt.show()

cv2.imwrite('gray.png', img) #to save the img file