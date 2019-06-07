#!/usr/bin/env python3
#
# Video Capture exercise
#
#

import cv2
import numpy as np
from matplotlib import pyplot as plt

device = 0
cam = cv2.VideoCapture(device)

if cam.isOpened() == False:
    print("Error opening camera")
    # Release resources, even if it errored out
    cam.release()
else:
	while cam.isOpened():
		# Capture frame-by-frame
		ret, frame = cam.read()
		if ret == False:
			print("End of video")
			break;
		plt.imshow(frame)
		plt.show()
	cam.release()

cv2.destroyAllWindows()
