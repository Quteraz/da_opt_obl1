import numpy as np
import csv
import os

os.makedirs('datasets', exist_ok=True)
print('\nGenerating data')
data_100 = np.random.randint(1, 100, size=(100,100))
data_1000 = np.random.randint(1, 100, size=(1000,1000))
data_5000 = np.random.randint(1, 100, size=(5000,5000))
data_10000 = np.random.randint(1, 100, size=(10000,10000))
print('Done\n-------------------------------------------------------------------------------------')

print('\nWriting to file')


with open('datasets/data_1000', 'w') as csvfile:
	writer = csv.writer(csvfile)
	writer.writerows(data_1000)

with open('datasets/data_5000', 'w') as csvfile:
	writer = csv.writer(csvfile)
	writer.writerows(data_5000)

with open('datasets/data_10000', 'w') as csvfile:
	writer = csv.writer(csvfile)
	writer.writerows(data_10000)
with open('datasets/data_100', 'w') as csvfile:
	writer = csv.writer(csvfile)
	writer.writerows(data_100)
print('Done\n-------------------------------------------------------------------------------------\n')
