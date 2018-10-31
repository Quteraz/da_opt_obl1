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
	return path

def random_iterative(data, count):
	# literally just random done count number of times
	best_path = random_normal(data)
	best_length = calc_length(best_path, data)
	for _ in range(count):
		new_path = random_normal(data)
		new_length = calc_length(new_path, data)
		if new_length < best_length:
			best_path = new_path
			best_length = new_length
	return best_path

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
	return path

def greedy_opt(path,data, iterations):
	# pick two random nodes
	# switch
	# re-calculate new path
	# if better keep
	length = calc_length(path, data)
	for _ in range(iterations):
		val1 = np.random.randint(0,len(path))
		val2 = np.random.randint(0,len(path))
		while val1 == val2:
			val2 = np.random.randint(0,len(path))
		
		new_path = cp.copy(path)
		new_path[val1], new_path[val2] = new_path[val2], new_path[val1]
		new_length = calc_length(new_path, data)
		if new_length < length:
			length = new_length
			path = new_path
	return path		

def greedy_random_opt(path, data, prob, iterations):

	length = calc_length(path, data)
	best_path = cp.copy(path)
	best_length = cp.copy(length)

	while prob > 0.001:
		for _ in range(iterations):
			val1 = np.random.randint(0,len(path))
			val2 = np.random.randint(0,len(path))
			while val1 == val2:
				val2 = np.random.randint(0,len(path))
			
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
				random = np.random.rand()
				if random < prob:
					length = new_length
					path = new_path
		prob *= 0.9
	return best_path
	
