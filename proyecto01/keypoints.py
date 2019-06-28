#!/usr/bin/env python3
import cv2 as cv
import numpy as np
import argparse
from AKAZE import akaze
from BRISK import brisk
from KAZE import kaze
from ORB import orb

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
			res = orb.ORB(prev_frame, frame)
			cv.imshow(orb.ORB.__name__, res)
			if cv.waitKey(25) & 0xFF == ord('q'):
				break
		else:
			break

	cap.release()
	cv.destroyAllWindows()

if __name__ == "__main__":
	main()
