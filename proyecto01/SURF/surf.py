import cv2 as cv
import numpy as np

def SURF(prev_frame, frame):
	## [load]
	gray0 = cv.cvtColor(prev_frame, cv.COLOR_BGR2GRAY)
	gray1 = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
	## [load]

	## [SURF]
	surf = cv.xfeatures2d.SURF_create()
	t1d = cv.getTickCount()
	kpts0, desc0 = surf.detectAndCompute(gray0, None)
	kpts1, desc1 = surf.detectAndCompute(gray1, None)
	t2d = cv.getTickCount()

	# time for detection
	tDetectSurf = 1000 * (t2d - t1d) / cv.getTickFrequency()
	## [SURF]

	## [Brute-Force matching]
	matcher = cv.BFMatcher(cv.NORM_L2, crossCheck=False)
	t1m = cv.getTickCount()
	matches = matcher.knnMatch(desc0, desc1, 2)
	t2m = cv.getTickCount()

	# time for matching
	tMatchSurf = 1000 * (t2m - t1m) / cv.getTickFrequency()
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
	print('# Keypoints 1:                                        \t', len(kpts0))
	print('# Keypoints 2:                                        \t', len(kpts1))
	print('# Matches:                                            \t', len(matched))
	print('# Detection and Description Time (ms):                \t', tDetectSurf)
	print('# Matching Time (ms):                                  \t', tMatchSurf)

	return res
	## [RESULTS]
