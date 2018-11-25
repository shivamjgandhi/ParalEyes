import numpy as np 
import cv2

cap = cv2.VideoCapture(0)
index = 0

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Display the resulting frame
    newframe = frame[:,:,0]
    newframe[210:240, 299:301] = 255
    newframe[210:212, 255:300] = 255
    newframe[210:240, 255:257] = 255
    newframe[238:240, 255:300] = 255

    newframe[210:240, 325:327] = 255
    newframe[210:212, 327:372] = 255
    newframe[210:240, 370:372] = 255
    newframe[238:240, 327:372] = 255

    cv2.imshow('frame', newframe)
    cv2.imwrite('C:/Users/Sjgandhi1998/Desktop/ParalEyes/training_data/img' + str(index) + '.png', newframe)
    index = index + 1
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
