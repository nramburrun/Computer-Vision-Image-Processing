import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
	_, frame = cap.read() # _ cause we dont really care about that value
	hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)  #heu-sat-value. HEU - COLOR. VALUE - HOW MUCH OF THAT COLOR EXISTS. SAT- HOW INTENSE IT IS
	
	# hue sat value
	lower = np.array([150,150,50])
	upper = np.array([180,255,150])

	mask = cv2.inRange(hsv,lower,upper) #mask is everything within this range. its a boolean, if range, 1
	result = cv2.bitwise_and(frame, frame,mask=mask) #mask will either be 0 or 1 based on inRange. So wherever the mask is 1, the color of the framew will be shown

	kernel = np.ones((15,15), np.float32)/225
	smoothed = cv2.filter2D(result,-1,kernel)

	cv2.imshow('frame',frame)
	cv2.imshow('result',result)
	cv2.imshow('smoothed', smoothed)
	k = cv2.waitKey(5) & 0xFF
	if k == 27:
		break

cv2.destroyAllWindows()
cap.release()

