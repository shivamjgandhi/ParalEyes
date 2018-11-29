# This script simply resizes all of the training data
from imageProcessing import lowerImageResolution
import os
import numpy as np 
import cv2

dirList = ['training_data/train/center',
'training_data/train/closed',
'training_data/train/left',
'training_data/train/right',
'training_data/train/up',
'training_data/validation/center',
'training_data/validation/closed',
'training_data/validation/left',
'training_data/validation/right',
'training_data/validation/up'
]

for directory in dirList:
	for filename in os.listdir(directory):
		if filename.endswith(".png"):
			img = cv2.imread(filename)
			newImg = lowerImageResolution(img, 0.5)
			os.remove(filename)
			cv2.imwrite('C:/Users/Sjgandhi1998/Desktop/ParalEyes/' + directory + filename, newframe)
			continue
		else:
			continue
