#!/usr/bin/env python3

import numpy as np
import argparse
import cv2

import argparse

def displayCamera():
	print ("displayCamera")

def meanShift():
	print ("meanShift")

def watershed():
	print ("watershed")

def slic():
	print ("slic")

def main():
	args.segmentation()

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
	
