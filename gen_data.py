import numpy as np
import csv

data_100 = np.random.randint(1, 300, size=(100,100))
data_1000 = np.random.randint(1, 300, size=(1000,1000))
data_10000 = np.random.randint(1, 300, size=(10000,10000))

with open('datasets/data_100', 'w') as csvfile:
	writer = csv.writer(csvfile)
	writer.writerows(data_100)

with open('datasets/data_1000', 'w') as csvfile:
	writer = csv.writer(csvfile)
	writer.writerows(data_1000)

with open('datasets/data_10000', 'w') as csvfile:
	writer = csv.writer(csvfile)
	writer.writerows(data_10000)