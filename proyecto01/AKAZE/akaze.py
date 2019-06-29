import cv2 as cv
import numpy as np

def AKAZE(prev_frame, frame):
	## [load]
	gray0 = cv.cvtColor(prev_frame, cv.COLOR_BGR2GRAY)
	gray1 = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
	## [load]

	## [A-KAZE]
	akaze = cv.AKAZE_create()
	t1d = cv.getTickCount()
	kpts0, desc0 = akaze.detectAndCompute(gray0, None)
	kpts1, desc1 = akaze.detectAndCompute(gray1, None)
	t2d = cv.getTickCount()

	# time for detection
	tDetectAkaze = 1000 * (t2d - t1d) / cv.getTickFrequency()
	## [A-KAZE]

	## [Brute-Force matching]
	matcher = cv.BFMatcher(cv.NORM_L2, crossCheck=False)
	t1m = cv.getTickCount()
	matches = matcher.knnMatch(desc0, desc1, 2)
	t2m = cv.getTickCount()

	# time for matching
	tMatchAkaze = 1000 * (t2m - t1m) / cv.getTickFrequency()
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
	print('\nA-KAZE Matching Results')
	print('*******************************')
	print('# Keypoints 1:                        \t', len(kpts0))
	print('# Keypoints 2:                        \t', len(kpts1))
	print('# Matches:                            \t', len(matched))
	print('# Detection Time (ms):                \t', tDetectAkaze)
	print('# Matching Time (ms):                 \t', tMatchAkaze)

	return res
	## [RESULTS]
