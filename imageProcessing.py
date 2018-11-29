import cv2
import numpy as np 
import scipy.misc

def lowerImageResolution(img, ratio):
	return scipy.misc.imresize(img, ratio)

