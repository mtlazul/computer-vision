#!/usr/bin/env python3
import cv2 as cv
import numpy as np
import argparse
from AKAZE import akaze
from BRISK import brisk
from KAZE import kaze
from ORB import orb
from SIFT import sift
from SURF import surf

def main():
	if args.keypoints:
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
				res = args.keypoints(prev_frame, frame)
				cv.imshow(args.keypoints.__name__, res)
				if cv.waitKey(25) & 0xFF == ord('q'):
					break
			else:
				break

		cap.release()
		cv.destroyAllWindows()
	else:
		print("\n\t\tPlease select a feature matching algorithm\n");
		parser.print_help()

if __name__ == "__main__":
	parser = argparse.ArgumentParser(description="Feature matching algorithms")
	parser.add_argument('--akaze', dest='keypoints', action='store_const',
						const=akaze.AKAZE, default=None,
						help='Apply A-KAZE algorithm for feature matching')
	parser.add_argument('--brisk', dest='keypoints', action='store_const',
						const=brisk.BRISK, default=None,
						help='Apply BRISK algorithm for feature matching')
	parser.add_argument('--kaze', dest='keypoints', action='store_const',
						const=kaze.KAZE, default=None,
						help='Apply KAZE algorithm for feature matching')
	parser.add_argument('--orb', dest='keypoints', action='store_const',
						const=orb.ORB, default=None,
						help='Apply ORB algorithm for feature matching')
	parser.add_argument('--sift', dest='keypoints', action='store_const',
						const=sift.SIFT, default=None,
						help='Apply SIFT algorithm for feature matching')
	parser.add_argument('--surf', dest='keypoints', action='store_const',
						const=surf.SURF, default=None,
						help='Apply SURF algorithm for feature matching')
	args = parser.parse_args()
	main()
