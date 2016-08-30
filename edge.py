import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
	_, frame = cap.read() # _ cause we dont really care about that value
	
	laplacian = cv2.Laplacian(frame, cv2.CV_64F)




	cv2.imshow('laplacian', laplacian)


	k = cv2.waitKey(5) & 0xFF
	if k == 27:
		break

cv2.destroyAllWindows()
cap.release()

