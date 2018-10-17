import numpy as np
import csv

with open('datasets/data_1000', 'r') as csvfile:
	reader = csv.reader(csvfile)
	data = {'short':list(reader)}
with open('datasets/data_5000', 'r') as csvfile:
	reader = csv.reader(csvfile)
	data['medium'] = list(reader)
with open('datasets/data_10000', 'r') as csvfile:
	reader = csv.reader(csvfile)
	data['large'] = list(reader)

data_template = {
		'short': {
			'path':[],
			'length':0
		},
		'medium': {
			'path':[],
			'length':0
		},
		'large': {
			'path':[],
			'length':0
		}
	}

def random_normal():
	# find random path
	# path = [np.random.permutation(1000),np.random.permutation(5000),np.random.permutation(10000)]
	# Length in the format of [length of set 1000, length of set 5000, length of set 10000]
	path_data = data_template
	for i in path_data:
		path_data[i]['length'] = 0
	path_data['short']['path'] = np.random.permutation(1000)
	path_data['medium']['path'] = np.random.permutation(5000)
	path_data['large']['path'] = np.random.permutation(10000)

	# iterate for each data set
	for i in path_data:
		last_pos = path_data[i]['path'][0]
		for current_pos in path_data[i]['path']:
			if last_pos == current_pos:
				path_data[i]['length'] += 0
			else:
				path_data[i]['length'] += int(data[i][last_pos][current_pos])
			last_pos = current_pos

	return path_data

def random_iterative(ant):
	# literally just random done ant number of times
	path_data = random_normal()
	# print(path_data)
	for _ in range(ant):
		new_data = random_normal()
		for element in new_data:
			if new_data[element]['length'] < path_data[element]['length']:
				path_data[element] = new_data[element]
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

random_data = random_normal()
# random_iterative_data = random_iterative(1000)
# greedy_data = greedy()

print('\nGenerating paths')
print('-------------------------------------------------------------------------------------')
print('Random')
for e in random_data:
	print('Length in',e,':',random_data[e]['length'])
print('-------------------------------------------------------------------------------------')
random_data = random_iterative(1000)
print('Random Iterative')
for e in random_data:
	print('Length: ',random_data[e]['length'])
print('-------------------------------------------------------------------------------------')
# print('Greedy')
# for e in greedy_data:
# 	print('Length: ',greedy_data[e]['length'])
# print('-------------------------------------------------------------------------------------\n')