import numpy as np
import csv

def random_normal():
	with open('datasets/data_100', 'r') as csvfile:
		reader = csv.reader(csvfile)
		print (reader)

random_normal()