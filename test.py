from imageProcessing import lowerImageResolution
import cv2
import numpy as np 

testImg = cv2.imread('testImg.jpg')
reducedImg = lowerImageResolution(testImg, 0.2)
cv2.imshow('image', reducedImg)
cv2.waitKey(0)
cv2.destroyAllWindows()

