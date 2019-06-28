#! /usr/bin/python

from __future__ import print_function
import cv2 as cv
import numpy as np
import argparse
from math import sqrt


def BRISK(prev_frame, frame):
	## [load]
	gray0 = cv.cvtColor(prev_frame, cv.COLOR_BGR2GRAY)
	gray1 = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
	## [load]

	## [BRISK]
	brisk = cv.BRISK_create()
	kpts0, desc0 = brisk.detectAndCompute(gray0, None)
	kpts1, desc1 = brisk.detectAndCompute(gray1, None)
	## [BRISK]

	## [Brute-Force matching]
	# cv.NORM_HAMMING should be used for binary string based descriptor (e.g. ORB, BRISK)
	# crossCheck ON for better results
	matcher = cv.BFMatcher(cv.NORM_HAMMING, crossCheck=True)
	matches = matcher.match(desc0, desc1)
	matches = sorted(matches, key = lambda x:x.distance) # Sort them in the order of their distance
	## [Brute-Force matching]

	## [draw final matches]
	res = np.empty((max(gray0.shape[0], gray1.shape[0]), gray0.shape[1]+gray1.shape[1], 3), dtype=np.uint8)
	cv.drawMatches(gray0, kpts0, gray1, kpts1, matches, res, flags=cv.DRAW_MATCHES_FLAGS_NOT_DRAW_SINGLE_POINTS)
	## [draw final matches]

	## [RESULTS]
	print('\nBRISK Matching Results')
	print('*******************************')
	print('# Keypoints 1:                        \t', len(kpts0))
	print('# Keypoints 2:                        \t', len(kpts1))
	print('# Matches:                            \t', len(matches))

	return res
	## [RESULTS]


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
			res = BRISK(prev_frame, frame)
			cv.imshow(BRISK.__name__, res)
			if cv.waitKey(25) & 0xFF == ord('q'):
				break
		else:
			break

	cap.release()
	cv.destroyAllWindows()


if __name__ == "__main__":
	main()
