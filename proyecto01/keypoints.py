#!/usr/bin/env python3
import cv2 as cv
import numpy as np
import argparse
from AKAZE import akaze
from BRISK import brisk

def main():
	cap = cv.VideoCapture(0)
	if (cap.isOpened()== False):
		print("Error opening camera stream")
		cap.release()
		return

	ret, frame = cap.read()
	while(cap.isOpened()):
		prev_frame = frame[:]
		ret, frame = cap.read()
		if ret == True:
			res = brisk.BRISK(prev_frame, frame)
			cv.imshow(brisk.BRISK.__name__, res)
			if cv.waitKey(25) & 0xFF == ord('q'):
				break
		else:
			break

	cap.release()
	cv.destroyAllWindows()

if __name__ == "__main__":
	main()
