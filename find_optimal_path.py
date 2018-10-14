import numpy as np
import csv

with open('datasets/data_1000', 'r') as csvfile:
	reader = csv.reader(csvfile)
	data = [list(reader)]
with open('datasets/data_5000', 'r') as csvfile:
	reader = csv.reader(csvfile)
	data.append(list(reader))
with open('datasets/data_10000', 'r') as csvfile:
	reader = csv.reader(csvfile)
	data.append(list(reader))

def random_normal():
	# find random path
	path = [np.random.permutation(1000),np.random.permutation(5000),np.random.permutation(10000)]
	# Length in the format of [length of set 1000, length of set 5000, length of set 10000]
	length = [0,0,0]

	# iterete for each data set
	for i in range(3):
		last_pos = path[i][0]
		for current_pos in path[i]:
			if last_pos == current_pos:
				length[i] += 0
			else:
				length[i] += int(data[i][last_pos][current_pos])
			last_pos = current_pos

	path_data = {
		'short': {
			'path':path[0],
			'length':length[0]
		},
		'medium': {
			'path':path[1],
			'length':length[1]
		},
		'large': {
			'path':path[2],
			'length':length[2]
		}
	}
	return path_data

def random_iterative(ant):
	# literally just freedy done ant number of times
	path_data = random_normal()
	# print(path_data)
	for _ in range(ant):
		new_data = random_normal()
		for element in new_data:
			print(new_data[element]['length'],path_data[element]['length'])
			if new_data[element]['length'] < path_data[element]['length']:
				print('Hey')
				path_data[element] = element
	return path_data

def greedy():
	pos = [np.random.randint(1000),np.random.randint(5000),np.random.randint(10000)]
	start = pos
	marked = [[0]*1000,[0]*5000,[0]*10000]
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
		length[i] += int(data[i][start[i]][pos[i]])
	return length


print('\nGenerating paths')
# print('-------------------------------------------------------------------------------------')
# print ('Random\nLength: ',random_normal())
print('-------------------------------------------------------------------------------------')
print('Random Iterative\nLength:',random_iterative(1000))
print('-------------------------------------------------------------------------------------')
print('Greedy\nLength:',greedy())
print('-------------------------------------------------------------------------------------\n')