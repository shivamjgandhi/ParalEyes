# ParalEyes
This is a deep learning model that allows paralyzed people to communicate using eye movements. The model classifies the orientation of their eyes, and using a "code", it turns triples of orientations into letters and spaces.

MODULES:
- paralEyes: main module that is executed. Reads in the video data
- trainCNN: trains the neural net 
- imageProcessing: module that contains functions that reduce the image resolution so they're easier to work with
- resizeTrainingDir: single run module that resizes all images in the training_data directory

DIRECTORIES:
training_data: data that's used for training in trainCNN
