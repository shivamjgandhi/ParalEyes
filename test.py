from imageProcessing import lowerImageResolution
import cv2
import numpy as np 

testImg = cv2.imread('training_data/train/center/img3.png')
print(testImg.size)
cv2.imshow('image', testImg)
cv2.waitKey(0)
cv2.destroyAllWindows()

