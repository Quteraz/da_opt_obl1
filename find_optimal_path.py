import numpy as np
import csv

with open('datasets/data_100', 'r') as csvfile:
	reader = csv.reader(csvfile)
	data = [list(reader)]
with open('datasets/data_1000', 'r') as csvfile:
	reader = csv.reader(csvfile)
	data.append(list(reader))
with open('datasets/data_10000', 'r') as csvfile:
	reader = csv.reader(csvfile)
	data.append(list(reader))

def random_normal():
	path = [np.random.permutation(100),np.random.permutation(1000),np.random.permutation(10000)]

	length = [0,0,0]
	for i in range(3):
		last_pos = path[i][0]
		for current_pos in path[i]:
			if last_pos == current_pos:
				length[i] += 0
			else:
				length[i] += int(data[i][last_pos][current_pos])
			last_pos = current_pos
	return length

def random_iterative(ant):
	length = random_normal()
	for _ in range(ant):
		new_length = random_normal()
		for index, element in enumerate(new_length):
			if element < length[index]:
				length[index] = element
	return length

def greedy():
	pos = [np.random.randint(100),np.random.randint(1000),np.random.randint(10000)]

	marked = [[0]*100,[0]*1000,[0]*10000]
	length = [0,0,0]

	for i in range(3):
		marked[i][pos[i]] = 1
		for _ in marked[i]:
			val = -1
			search = data[i][pos[i]]
			for index, el in enumerate(search):
				el = int(el)
				if el < val and marked[i][index] != 1 or val < 0 and marked[i][index] != 1:
					val = el
					pos[i] = index
				else:
					pass
			length[i] += val
			marked[i][pos[i]] = 1
	return length



print('\n-------------------------------------------------------------------------------------')
print ('Random\nLength: ',random_normal())
print('-------------------------------------------------------------------------------------')
print('Random Iterative\nLength:',random_iterative(50))
print('-------------------------------------------------------------------------------------')
print('Greedy\ntest:',greedy())
print('-------------------------------------------------------------------------------------\n')