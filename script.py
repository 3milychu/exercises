# Get list of images from folder and save as csv

import os
import numpy as np

file_list = []
file_path = "/Volumes/Samsung_t3/pics"
for root, dirs, files in os.walk(file_path):
	for file in files:
		file_list.append(file)

np.savetxt('file_list.csv', file_list, fmt="%s", delimiter",")


# Read from CSV and conver to JSON

import numpy as np
import pandas as pd 
from matplotlib import pyplot as plt 

file_path = '/Volumes/Samsung_t3/pics/file_list.csv'
df = pd.read_csv(path)

print(df.head())
print(df.shape)

df['Index'] = df.indexn






