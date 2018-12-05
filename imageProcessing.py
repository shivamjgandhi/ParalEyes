import cv2
import numpy as np 
import scipy.misc

def lowerImageResolution(img, ratio):
	"""
	Lowers the image resolution such that it can be input into
	the neural net properly.
	"""
	return scipy.misc.imresize(img, ratio)
