import numpy as np
import csv

path_100 = np.random.permutation(100)
path_1000 = np.random.permutation(1000)
path_10000 = np.random.permutation(10000)

with open('datasets/path_100', 'w') as csvfile:
	writer = csv.writer(csvfile)
	writer.writerow(path_100)

with open('datasets/path_1000', 'w') as csvfile:
	writer = csv.writer(csvfile)
	writer.writerow(path_1000)

with open('datasets/path_10000', 'w') as csvfile:
	writer = csv.writer(csvfile)
	writer.writerow(path_1000)