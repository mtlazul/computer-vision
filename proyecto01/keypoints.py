#!/usr/bin/env python3
import cv2 as cv
import numpy as np
import argparse
import os
from AKAZE import akaze
from BRISK import brisk
from KAZE import kaze
from ORB import orb
from SIFT import sift
from SURF import surf

def main():
	if args.keypoints:
		in1_image = False
		in2_image = False
		cap1 = None
		cap2 = None
		print (1)

		root, ext = os.path.splitext(args.in1)
		if ext in ['.bmp','.dib', '.jpeg', '.jpg', '.jpe', '.jp2', '.png', '.webp', '.pbm', '.pgm', '.ppm', '.sr', '.ras', '.tiff', '.tif']:
			in1_image = True
			frame1 = cv.imread(args.in1)
			if frame1.size == 0:
				print("\n\t\tError opening input 1 image\n")
				if cap1 != None:
					cap1.release()
				if cap2 != None:
					cap2.release()
				return
		else:
			cap1 = cv.VideoCapture(args.in1)
			ret, frame1 = cap1.read()
			if (cap1.isOpened()== False):
				print("\n\t\tError opening input 1 video\n")
				if cap1 != None:
					cap1.release()
				if cap2 != None:
					cap2.release()
				return

		if args.in1 == args.in2:
			if not in1_image:
				cap2 = cap1
			frame2 = frame1
		else:
			root, ext = os.path.splitext(args.in2)
			if ext in ['.bmp','.dib', '.jpeg', '.jpg', '.jpe', '.jp2', '.png', '.webp', '.pbm', '.pgm', '.ppm', '.sr', '.ras', '.tiff', '.tif']:
				in2_image = True
				frame2 = cv.imread(args.in2)
				if frame2.size == 0:
					print("\n\t\tError opening input 2 image\n")
					if cap1 != None:
						cap1.release()
					if cap2 != None:
						cap2.release()
					return
				print (4)
			else:
				cap2 = cv.VideoCapture(args.in2)
				ret, frame2 = cap2.read()
				if (cap2.isOpened()== False):
					print("\n\t\tError opening input 2 video\n")
					if cap1 != None:
						cap1.release()
					if cap2 != None:
						cap2.release()
					return
				print (5)

		while(1):
			if not in1_image:
				if not cap1.isOpened():
					break
				ret, frame1 = cap1.read()
				if ret == False:
					break
			if not in2_image:
				if not cap2.isOpened():
					break
				ret, frame2 = cap2.read()
				if ret == False:
					break

			#frame2 = cv.resize(frame2, (frame1.shape[1],frame1.shape[0]), interpolation = cv.INTER_AREA)

			res = args.keypoints(frame1, frame2)
			cv.imshow(args.keypoints.__name__, res)
			if cv.waitKey(25) & 0xFF == ord('q'):
				break

		if cap1 != None:
			cap1.release()
		if cap2 != None:
			cap2.release()
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
	parser.add_argument('--in1', action="store", dest="in1",
						default="/dev/video0", type=str,
						help="First input of the feature matching algorithm. Can be a video device, image or video file")
	parser.add_argument('--in2', action="store", dest="in2",
						default="/dev/video0", type=str,
						help="Second input of the feature matching algorithm.  Can be a video device, image or video file")
	args = parser.parse_args()
	main()
