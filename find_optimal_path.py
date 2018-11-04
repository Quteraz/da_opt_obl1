import numpy as np
import csv
import copy as cp

def calc_length(path, data):
	# Data in the format of data[i][i]
	# path in the format of path[i]
	last_pos = path[0]
	length = 0
	for current_pos in path:
		if last_pos == current_pos:
			length += 0
		else:
			length += int(data[int(last_pos)][int(current_pos)])
		last_pos = current_pos
	return length 

def random_normal(data):
	# Data in the format of data[i][i]
	path = np.random.permutation(len(data[0]))
	length = calc_length(path, data)
	return path, length

def random_iterative(data, count):
	# literally just random done count number of times
	best_path, best_length = random_normal(data)
	for _ in range(count):
		new_path, new_length = random_normal(data)
		if new_length < best_length:
			best_path = new_path
			best_length = new_length
	return best_path, best_length

def greedy(data):

	path = []
	pos = np.random.randint(len(data[0]))
	marked = [0]*len(data[0])

	marked[pos] = 1
	for _ in marked:
		length = 0
		search = data[pos]
		for index, val in enumerate(search):
			if int(val) < length and marked[index] != 1 or length == 0 and marked[index] !=1:
				length = int(val)
				pos = index
			else:
				pass
		path = np.append(path, pos)
		marked[pos] = 1
	length = calc_length(path, data)
	return path, length

def greedy_opt(path, length, data, iterations):
	# pick two random nodes
	# switch
	# re-calculate new path
	# if better keep

	best_path = cp.copy(path)
	best_length = cp.copy(length)

	axis_y = []

	for _ in range(iterations):
		# Setting up values
		val1 = np.random.randint(0,len(path))
		val2 = np.random.randint(0,len(path))
		while val1 == val2:
			val2 = np.random.randint(0,len(path))
		
		# greedy part
		new_path = cp.copy(best_path)
		new_path[val1], new_path[val2] = new_path[val2], new_path[val1]
		new_length = calc_length(new_path, data)
		if new_length < best_length:
			best_length = new_length
			best_path = new_path

		# plotting
		axis_y += [best_length]
	return best_path, best_length, axis_y

def greedy_random_opt(path, length, data, prob, iterations):
	# greedy opt with a hint of randomness
	axis_y = []

	best_path = cp.copy(path)
	best_length = cp.copy(length)

	while prob > 0.001:
		for _ in range(iterations):
			# setting up values
			val1 = np.random.randint(0,len(path))
			val2 = np.random.randint(0,len(path))
			while val1 == val2:
				val2 = np.random.randint(0,len(path))
			# greedy part
			new_path = cp.copy(path)
			new_path[val1], new_path[val2] = new_path[val2], new_path[val1]
			new_length = calc_length(new_path, data)
			if new_length < length:
				length = new_length
				path = new_path
				if new_length < best_length:
					best_length = new_length
					best_path = new_path
			else:
				# random part based on prob
				random = np.random.rand()
				if random < prob:
					length = new_length
					path = new_path
			# plotting
		axis_y += [best_length]
		prob *= 0.9
	return best_path, best_length, axis_y