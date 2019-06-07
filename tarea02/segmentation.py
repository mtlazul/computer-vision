#!/usr/bin/env python3

import numpy as np
import argparse
import cv2

import argparse

def displayCamera(frame):
	return frame

def meanShift(frame):
	return frame

def watershed(frame):
	return frame

def slic(frame):
	return frame

def main():
	cap = cv2.VideoCapture(0)
	if (cap.isOpened()== False):
		print("Error opening camera stream")
		cap.release()
		return

	while(cap.isOpened()):
		ret, frame = cap.read()
		if ret == True:
			frame = args.segmentation(frame)
			cv2.imshow(args.segmentation.__name__,frame)
			if cv2.waitKey(25) & 0xFF == ord('q'):
				break
		else:
			break

	cap.release()
	cv2.destroyAllWindows()

if __name__ == "__main__":
	parser = argparse.ArgumentParser(description="Image level segmentation algorithms. "+
	"By default it only displays the camera stream. To apply an algorithm use one of the options")
	parser.add_argument('--ms', dest='segmentation', action='store_const',
						const=meanShift, default=displayCamera,
						help='Apply mean shift algorithm to the camera stream')
	parser.add_argument('--ws', dest='segmentation', action='store_const',
						const=watershed, default=displayCamera,
						help='Apply watershed algorithm to the camera stream')
	parser.add_argument('--slic', dest='segmentation', action='store_const',
						const=slic, default=displayCamera,
						help='Apply simple linear iterative clustering algorithm to the camera stream')
	args = parser.parse_args()
	main()
	
