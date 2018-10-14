import numpy as np
import csv
import os

os.makedirs('datasets', exist_ok=True)

data_1000 = np.random.randint(1, 300, size=(1000,1000))
data_5000 = np.random.randint(1, 300, size=(5000,5000))
data_10000 = np.random.randint(1, 300, size=(10000,10000))

with open('datasets/data_1000', 'w') as csvfile:
	writer = csv.writer(csvfile)
	writer.writerows(data_1000)

with open('datasets/data_5000', 'w') as csvfile:
	writer = csv.writer(csvfile)
	writer.writerows(data_5000)

with open('datasets/data_10000', 'w') as csvfile:
	writer = csv.writer(csvfile)
	writer.writerows(data_10000)