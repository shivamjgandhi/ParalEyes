import numpy as np  
import cv2
from keras.models import load_model
from imageProcessing import lowerImageResolution
from helperFunctions import *

cap = cv2.VideoCapture(0)
model = load_model('parlEyes_model.h5')
previousClassifications = np.zeros((1,30))
index = 0

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Display the resulting frame
    cv2.imshow('frame', newframe)

    # Extract the eyes out of the frame
    eyes = cv2.CascadeClassifier('haarcascade_eye.xml')
    detected = eyes.detectMultiScale(frame, 1.3, 5)

    # Classify image via neural net
    predictIxs = model.predict(frame, batch_size=None, verbose=0, steps=None)

    # Store value in memory bank

    # Check if memory bank warrants adding a new letter

    # If user did two long blinks, then end

    index = index + 1
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
