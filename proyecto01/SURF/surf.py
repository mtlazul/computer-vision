#! /usr/bin/python

from __future__ import print_function
import cv2 as cv
import numpy as np
import argparse
from math import sqrt


def SURF(prev_frame, frame):
	## [load]
	gray0 = cv.cvtColor(prev_frame, cv.COLOR_BGR2GRAY)
	gray1 = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
	## [load]

	## [SURF]
	surf = cv.xfeatures2d.SURF_create()
	kpts0, desc0 = surf.detectAndCompute(gray0, None)
	kpts1, desc1 = surf.detectAndCompute(gray1, None)
	## [SURF]

	## [Brute-Force matching]
	matcher = cv.BFMatcher()
	matches = matcher.knnMatch(desc0, desc1, 2)
	## [Brute-Force matching]

	## [ratio test filtering]
	matched = []
	match_ratio = 0.75
	for m,n in matches:
		if m.distance < match_ratio * n.distance:
			matched.append(m)
	## [ratio test filtering]

	## [draw final matches]
	res = np.empty((max(gray0.shape[0], gray1.shape[0]), gray0.shape[1]+gray1.shape[1], 3), dtype=np.uint8)
	cv.drawMatches(gray0, kpts0, gray1, kpts1, matched, res, flags=cv.DRAW_MATCHES_FLAGS_NOT_DRAW_SINGLE_POINTS)
	## [draw final matches]

	## [RESULTS]
	print('\nSURF Matching Results')
	print('*******************************')
	print('# Keypoints 1:                        \t', len(kpts0))
	print('# Keypoints 2:                        \t', len(kpts1))
	print('# Matches:                            \t', len(matched))

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
			res = SURF(prev_frame, frame)
			cv.imshow(SURF.__name__, res)
			if cv.waitKey(25) & 0xFF == ord('q'):
				break
		else:
			break

	cap.release()
	cv.destroyAllWindows()


if __name__ == "__main__":
	main()
