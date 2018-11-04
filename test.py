import find_optimal_path as op
import csv
import sys
import matplotlib.pyplot as plt

print('\nReading files')

# specify what data is being used
data_set = str(sys.argv[1])

if data_set == 'test':
	with open('datasets/data_100', 'r') as csvfile:
		reader = csv.reader(csvfile)
		data= list(reader)
elif data_set == 'small':
	with open('datasets/data_1000', 'r') as csvfile:
		reader = csv.reader(csvfile)
		data = list(reader)
elif data_set == 'medium':
	with open('datasets/data_5000', 'r') as csvfile:
		reader = csv.reader(csvfile)
		data = list(reader)
elif data_set == 'large':
	with open('datasets/data_10000', 'r') as csvfile:
		reader = csv.reader(csvfile)
		data = list(reader)
else:
	print('error: no dataset with matching values. exiting')
	quit()
	
print('Done\n-------------------------------------------------------------------------------------')

print('\nGenerating paths')
print('-------------------------------------------------------------------------------------')

print('Random')

random_data, random_length = op.random_normal(data)
print('Length in',data_set,':',random_length)

print('-------------------------------------------------------------------------------------')
print('Random Iterative')

random_iterative_data, iterative_length = op.random_iterative(data, 1000)
print('Length in',data_set,':',iterative_length)

print('-------------------------------------------------------------------------------------')
print('Greedy')

greedy_data, greedy_length = op.greedy(data)
print('Length of',data_set,':',greedy_length)

print('-------------------------------------------------------------------------------------')

print('\nGreedy Optimizing')
print('-------------------------------------------------------------------------------------')

iterations = 10000

print('Random')

opt_random_path, opt_random_length, random_plt = op.greedy_opt(random_data, random_length, data, iterations)
print('Length in',data_set,':',random_length)

print('-------------------------------------------------------------------------------------')
print('Random Iterative')

opt_iterative_path, opt_iterative_length, iterative_plt = op.greedy_opt(random_iterative_data, iterative_length, data, iterations)
print('Length in',data_set,':',iterative_length)

print('-------------------------------------------------------------------------------------')
print('Greedy')

opt_greedy_path, opt_greedy_length, greedy_plt = op.greedy_opt(greedy_data, greedy_length, data, iterations)
print('Length of',data_set,':',greedy_length)

print('-------------------------------------------------------------------------------------')

plt.subplot(211)
plt.title('Greedy Optimizing')
plt.xlabel('Iterations')
plt.ylabel('Length')
plt.plot(random_plt)
plt.plot(iterative_plt, 'r')
plt.plot(greedy_plt, 'g')

print('\nGreedy Random Optimizing')
print('-------------------------------------------------------------------------------------')

iterations = 100
prob = 0.9


print('Random')

opt_random_path, opt_random_length, random_plot = op.greedy_random_opt(random_data, random_length, data, prob, iterations)
print('Length in',data_set,':',random_length)

print('-------------------------------------------------------------------------------------')
print('Random Iterative')

opt_iterative_path, opt_iterative_length, iterative_plot = op.greedy_random_opt(random_iterative_data, iterative_length, data, prob, iterations)
print('Length in',data_set,':',iterative_length)

print('-------------------------------------------------------------------------------------')
print('Greedy')

opt_greedy_path, opt_greedy_length, greedy_plot = op.greedy_random_opt(greedy_data, greedy_length, data, prob, iterations)
print('Length of',data_set,':',greedy_length)

print('-------------------------------------------------------------------------------------\n')
plt.subplot(212)
plt.title('Greedy Random Optimizing')
plt.xlabel('Iterations')
plt.ylabel('Length')
plt.plot(random_plot)
plt.plot(iterative_plot, 'r')
plt.plot(greedy_plot, 'g')
plt.tight_layout()
plt.savefig('datasets/plotting.png')
plt.show()