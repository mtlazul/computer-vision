#!/usr/bin/env python3

import numpy as np
import argparse
import cv2
from skimage.util import img_as_float
from skimage.segmentation import slic
from sklearn.cluster import MeanShift, estimate_bandwidth
import json

def displayCamera(frame):
	return frame

def meanShift(frame):
	# Load params
	pram_file = open("meanshift.json")
	param = json.load(pram_file)
	# Convert capture space color to RGB
	rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
	frame = np.array(rgb_frame)
	# Original shape from new RGB frame
	orig_shape = frame.shape
	# Convert image into feature array based on RGB intensities
	flat_frame = np.reshape(frame, [-1, 3])
	# Mean Shift
	bandwidth = estimate_bandwidth(flat_frame,
					quantile = param["quantile"],
					n_samples = param["n_samples"],
					random_state = param["random_state"],
					n_jobs = param["n_jobs"])
	ms = MeanShift(bandwidth,
					bin_seeding = param["bin_seeding"],
					min_bin_freq = param["min_bin_freq"],
					cluster_all = param["cluster_all"],
					n_jobs = param["n_jobs"])
	ms.fit(flat_frame)
	labels = ms.labels_
	# Take size and ignore RGB channels
	segments = np.reshape(labels, orig_shape[:2])

	segment_img_gray = np.array(segments, dtype=np.uint8)
	segment_img_gray = segment_img_gray*(255//np.max(segments))
	segment_img_color = cv2.applyColorMap(segment_img_gray, cv2.COLORMAP_JET)
	return segment_img_color

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
	
