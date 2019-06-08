#!/usr/bin/env python3

import numpy as np
import argparse
import cv2
from skimage.util import img_as_float
from skimage.segmentation import slic
import json

import argparse

def displayCamera(frame):
	return frame

def meanShift(frame):
	return frame

def watershed(frame):
	return frame

def slicSegmentation(frame):
	pram_file = open("slic.json")
	param = json.load(pram_file)
	segments = slic(frame,
					n_segments = param["n_segments"],
					compactness = param["compactness"],
					max_iter = param["max_iter"],
					sigma = param["sigma"],
					multichannel = param["multichannel"],
					convert2lab = param["convert2lab"],
					enforce_connectivity = param["enforce_connectivity"],
					min_size_factor = param["min_size_factor"],
					max_size_factor = param["max_size_factor"],
					slic_zero = param["slic_zero"])
	segment_img_gray = np.array(segments, dtype=np.uint8)
	segment_img_gray = segment_img_gray*(255//np.max(segments))
	segment_img_color = cv2.applyColorMap(segment_img_gray, cv2.COLORMAP_JET)
	return segment_img_color

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
						const=slicSegmentation, default=displayCamera,
						help='Apply simple linear iterative clustering algorithm to the camera stream')
	args = parser.parse_args()
	main()
	
