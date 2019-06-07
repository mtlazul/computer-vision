#!/usr/bin/env python3
#
# Video Capture exercise
#
#

import cv2
import numpy as np

device = 0
cap = cv2.VideoCapture(device)

if (cap.isOpened()== False):
	print("Error opening camera stream")
	cap.release()

while(cap.isOpened()):
	ret, frame = cap.read()
	if ret == True:
		cv2.imshow('camera capture', frame)
		if cv2.waitKey(25) & 0xFF == ord('q'):
			break
	else:
		break

cap.release()
cv2.destroyAllWindows()
