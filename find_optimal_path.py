import numpy as np
import csv

with open('datasets/data_100', 'r') as csvfile:
	reader = csv.reader(csvfile)
	data_100 = list(reader)
with open('datasets/data_1000', 'r') as csvfile:
	reader = csv.reader(csvfile)
	data_1000 = list(reader)
with open('datasets/data_10000', 'r') as csvfile:
	reader = csv.reader(csvfile)
	data_10000 = list(reader)

def random_normal():
	path_100 = np.random.permutation(100)
	path_1000 = np.random.permutation(1000)
	path_10000 = np.random.permutation(10000)


	length = [0,0,0]

	last_pos = path_100[0]
	for path in path_100:
		if last_pos == path:
			length[0] += 0
		else: 
			length[0] += int(data_100[last_pos][path])
		last_pos = path

	last_pos = path_1000[0]
	for path in path_1000:
		if last_pos == path:
			length[1] += 0
		else: 
			length[1] += int(data_1000[last_pos][path])
		last_pos = path
		print(last_pos)

	last_pos = path_10000[0]
	for path in path_10000:
		if last_pos == path:
			length[2] += 0
		else: 
			length[2] += int(data_10000[last_pos][path])
		last_pos = path
	print ('length: ',length)
	return length

def random_iterative(ant):
	length = random_normal()
	for _ in range(ant):
		new_length = random_normal()
		if new_length < length:
			length = new_length
	print('Final length:',length)

def greedy():
	print('greedy')

random_normal()
print('-------------------------------------------------------------------------------------')
random_iterative(50)