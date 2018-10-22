import numpy as np
import csv
import copy

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
			'path':np.array([]),
			'length':0
		},
		'medium': {
			'path':np.array([]),
			'length':0
		},
		'large': {
			'path':np.array([]),
			'length':0
		}
	}

def random_normal():
	# find random path
	# path = [np.random.permutation(1000),np.random.permutation(5000),np.random.permutation(10000)]
	# Length in the format of [length of set 1000, length of set 5000, length of set 10000]
	path_data = copy.deepcopy(data_template)
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
				path_data[element]['length'] = new_data[element]['length']
				path_data[element]['path'] = new_data[element]['path']
	return path_data

def greedy():

	path_data = copy.deepcopy(data_template)
	for i in path_data:
		path_data[i]['length'] = 0
	path_data['short']['path'] = []
	path_data['medium']['path'] = []
	path_data['large']['path'] = []

	mark_pos = {
		'short': {
			'pos':np.random.randint(1000),
			'marked':[0]*1000
		},
		'medium': {
			'pos':np.random.randint(5000),
			'marked':[0]*5000
		},
		'large': {
			'pos':np.random.randint(10000),
			'marked':[0]*10000
		}
	}

	for el in mark_pos:
		mark_pos[el]['marked'][mark_pos[el]['pos']] = 1
		for _ in mark_pos[el]['marked']:
			length = 0
			search = data[el][mark_pos[el]['pos']]
			for index, val in enumerate(search):
				if int(val) < length and mark_pos[el]['marked'][index] != 1 or length == 0 and mark_pos[el]['marked'][index] !=1:
					length = int(val)
					mark_pos[el]['pos'] = index
				else:
					pass
			path_data[el]['length'] += length
			path_data[el]['path'] = np.append(path_data[el]['path'], mark_pos[el]['pos'])
			mark_pos[el]['marked'][mark_pos[el]['pos']] = 1
	return path_data

def random_opt(path, ant):
	# pick two random nodes
	# switch
	# re-calculate new path
	# if better keep
	for _ in range(ant):
		for el in data:
			val1 = np.random.randint(0,len(el))
			val2 = np.random.randint(0,len(el))
			while val1 == val2:
				val2 = np.random.randint(0,len(el))

			sub1 = int(data[el][path[el]['path'][val1-1]][path[el]['path'][val1]]) + int(data[el][path[el]['path'][val1]][path[el]['path'][val1+1]])
			sub2 = int(data[el][path[el]['path'][val2-1]][path[el]['path'][val2]]) + int(data[el][path[el]['path'][val2]][path[el]['path'][val2+1]])
			add1 = int(data[el][path[el]['path'][val1-1]][path[el]['path'][val2]]) + int(data[el][path[el]['path'][val2]][path[el]['path'][val1+1]])
			add2 = int(data[el][path[el]['path'][val2-1]][path[el]['path'][val1]]) + int(data[el][path[el]['path'][val1]][path[el]['path'][val2+1]])

			length = path[el]['length'] - sub1 - sub2 + add1 + add2
			if length < path[el]['length']:
				path[el]['length'] = length 
				placeholder = path[el]['path'][val1]
				path[el]['path'][val1] = path[el]['path'][val2]
				path[el]['path'][val2] = placeholder
	return path		

# def random_greedy_opt():
	# do stuff

random_data = random_normal()
random_iterative_data = random_iterative(1000)
greedy_data = greedy()

print('\nGenerating paths')
print('-------------------------------------------------------------------------------------')
print('Random')
for e in random_data:
	print('Length in',e,':',random_data[e]['length'])
print('-------------------------------------------------------------------------------------')
print('Random Iterative')
for e in random_iterative_data:
	print('Length in',e,':',random_iterative_data[e]['length'])
print('-------------------------------------------------------------------------------------')
print('Greedy')
for e in greedy_data:
	print('Length of',e,':',greedy_data[e]['length'])
print('-------------------------------------------------------------------------------------')

random_opt(random_data, 1000)
random_opt(random_iterative_data, 1000)
random_opt(greedy_data, 1000)

print('\nOptimizing paths')
print('-------------------------------------------------------------------------------------')
print('Random')
for e in random_data:
	print('Length in',e,':',random_data[e]['length'])
print('-------------------------------------------------------------------------------------')
print('Random Iterative')
for e in random_iterative_data:
	print('Length in',e,':',random_iterative_data[e]['length'])
print('-------------------------------------------------------------------------------------')
print('Greedy')
for e in greedy_data:
	print('Length of',e,':',greedy_data[e]['length'])
print('-------------------------------------------------------------------------------------\n')