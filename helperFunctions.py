import operator

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
	readings: updated readings

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
