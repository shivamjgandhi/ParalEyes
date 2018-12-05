import operator
import cv2
from skimage.transform import resize 

def changeState(current_state, readings):
	"""
	This function decides whether or not the user is trying to
	look in a new direction. If yes, then it changes the state.

	Inputs:
	current_state: current direction the user is looking
	readings: what direction the neural net decided that
	the user is looking for the past 30 frames

	Outputs: 
	new_state: the new direction that the user is looking
	"""
	count = {
	0: 0
	1: 0,
	2: 0,
	3: 0,
	4: 0
	}
	for x in readings:
		count[x] = count[x] + 1

	max_val = max(dict.iteritems(), key=operator.itemgetter(1))[0]

	if (max_val == current_state):
		return current_state
	else:
		if (count[max_val] > 20):
			return max_val

def updateReadings(current_state, new_state, readings):
	"""
	This function updates the memory bank in case the new state
	is different from the old one.

	Inputs: 
	current_state: which state the machine is currently at
	new_state: the new direction the user is looking at
	readings: previous memory of where the user was looking

	Outputs:
	readings: updated reading
	"""
	if (new_state != current_state):
		return readings[1:29].append(new_state)
	else:
		return readings

def printLetter(readings):
	"""
	This function prints a new letter if the user has completed
	a triple of looking in different directions.
	"""
	triple = (readings[27], readings[28], readings[29])
	if (triple == (0,0,0)):
		return "a"
	elif (triple == (0,0,1)):
		return "b"

def detectEyes(frame):
	"""
	This function uses a CascadeClassifier to detect where the
	eyes are and then returns the coordinates of the eye as well
	as the bounding box
	"""
	eyes = cv2.CascadeClassifier('haarcascade_eye.xml')
	detected = eyes.detectMultiScale(frame, 1.3, 5)
	return detected

def resizeEyes(frame, detected):
	"""
	Resizes the eye images so that they can be put into the neural
	net effectively. 

	INPUTS:
	- frame: a grayscale copy of the original image
	- detected: bounding box of where the eyes are in the image

	OUTPUTS:
	- resized image of eyes such that they're of size 42x42
	"""
	if (len(detected) > 0):
		rectangle = detected[0]
		eyes = frame[rectangle[0]:(rectangle[0] + rectangle[2]), rectangle[1]:(rectangle[1] + rectangle[3])]
		return resize(eyes, (42, 42))
	else:
		return False