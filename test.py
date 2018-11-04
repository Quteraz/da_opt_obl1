import find_optimal_path as op
import csv
import sys

print('\nReading files')
with open('datasets/data_1000', 'r') as csvfile:
	reader = csv.reader(csvfile)
	data_file = {'small':list(reader)}
with open('datasets/data_5000', 'r') as csvfile:
	reader = csv.reader(csvfile)
	data_file['medium'] = list(reader)
with open('datasets/data_10000', 'r') as csvfile:
	reader = csv.reader(csvfile)
	data_file['large'] = list(reader)
with open('datasets/data_100', 'r') as csvfile:
	reader = csv.reader(csvfile)
	data_file['test'] = list(reader)
print('Done\n-------------------------------------------------------------------------------------')

print('\nGenerating paths')
print('-------------------------------------------------------------------------------------')

# specify what data is being used
data_set = str(sys.argv[1])
data = data_file[data_set]

# Generating paths
random_data = op.random_normal(data)
random_iterative_data = op.random_iterative(data, 1000)
greedy_data = op.greedy(data)

print('Random')

random_length = op.calc_length(random_data, data)
print('Length in',data_set,':',random_length)

print('-------------------------------------------------------------------------------------')
print('Random Iterative')

iterative_length = op.calc_length(random_iterative_data, data)
print('Length in',data_set,':',iterative_length)

print('-------------------------------------------------------------------------------------')
print('Greedy')

greedy_length = op.calc_length(greedy_data, data)
print('Length of',data_set,':',greedy_length)

print('-------------------------------------------------------------------------------------')

print('\nGreedy Optimizing')
print('-------------------------------------------------------------------------------------')

iterations = 10000

opt_random_path = op.greedy_opt(random_data, data, iterations)
opt_iterative_path = op.greedy_opt(random_iterative_data, data, iterations)
opt_greedy_path = op.greedy_opt(greedy_data, data, iterations)

print('Random')

random_length = op.calc_length(opt_random_path, data)
print('Length in',data_set,':',random_length)

print('-------------------------------------------------------------------------------------')
print('Random Iterative')

iterative_length = op.calc_length(opt_iterative_path, data)
print('Length in',data_set,':',iterative_length)

print('-------------------------------------------------------------------------------------')
print('Greedy')

greedy_length = op.calc_length(opt_greedy_path, data)
print('Length of',data_set,':',greedy_length)

print('-------------------------------------------------------------------------------------')

print('\nGreedy Random Optimizing')
print('-------------------------------------------------------------------------------------')

iterations = 10000
prob = 0.9

opt_random_path = op.greedy_random_opt(random_data, data,prob, iterations)
opt_iterative_path = op.greedy_random_opt(random_iterative_data, data, prob, iterations)
opt_greedy_path = op.greedy_random_opt(greedy_data, data, prob, iterations)

print('Random')

random_length = op.calc_length(opt_random_path, data)
print('Length in',data_set,':',random_length)

print('-------------------------------------------------------------------------------------')
print('Random Iterative')

iterative_length = op.calc_length(opt_iterative_path, data)
print('Length in',data_set,':',iterative_length)
print('-------------------------------------------------------------------------------------')
print('Greedy')

greedy_length = op.calc_length(opt_greedy_path, data)
print('Length of',data_set,':',greedy_length)

print('-------------------------------------------------------------------------------------\n')