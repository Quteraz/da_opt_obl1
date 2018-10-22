import find_optimal_path as op
import csv

print('\nReading files')
with open('datasets/data_1000', 'r') as csvfile:
	reader = csv.reader(csvfile)
	data_file = {'short':list(reader)}
with open('datasets/data_5000', 'r') as csvfile:
	reader = csv.reader(csvfile)
	data_file['medium'] = list(reader)
with open('datasets/data_10000', 'r') as csvfile:
	reader = csv.reader(csvfile)
	data_file['large'] = list(reader)
with open('datasets/data_5000', 'r') as csvfile:
	reader = csv.reader(csvfile)
	data_file['test'] = list(reader)
print('Done\n-------------------------------------------------------------------------------------')

print('\nGenerating paths')
print('-------------------------------------------------------------------------------------')

data = data_file['test']
random_data = op.random_normal(data)
random_iterative_data = op.random_iterative(data, 1000)
greedy_data = op.greedy(data)

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

print('\nGreedy Optimizing')
print('-------------------------------------------------------------------------------------')

iterations = 10000

op.greedy_opt(random_data, data, iterations)
op.greedy_opt(random_iterative_data, data, iterations)
op.greedy_opt(greedy_data, data, iterations)

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