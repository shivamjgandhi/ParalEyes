import numpy as np 
import cv2
import os

cap = cv2.VideoCapture(0)
index = 0
directory = 'C:/Users/Sjgandhi1998/Software/ParalEyes/training_data/train/closed'

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    cv2.imshow('frame', frame)
    print(frame)
    cv2.imwrite(directory + '/img' + str(index) + '.png', frame)
    index = index + 1
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
