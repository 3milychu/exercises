# Get list of images from an API

import requests
api_url = 'http://127.0.0.1:5000/api/all'
r = requests.get(api_url)
print(r.status_code)
data_json= r.json()
pd.DataFrame(data_json).to_csv('data.csv', index=False)


# Get list of images from folder and save as csv

import os
import numpy as np

file_list = []
file_path = "/Volumes/Samsung_t3/project-repos/exercises/pics"
for root, dirs, files in os.walk(file_path):
    for file in files:
        file_list.append(file)
        
print(len(file_list))
        
np.savetxt('file.csv', file_list, fmt="%s", delimiter = ",")


# Read from CSV 

import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

file_path = "/Volumes/Samsung_t3/project-repos/exercises/file.csv"
df = pd.read_csv(file_path)


# Check the data and adjust/add new information as needed

print(df.head())
df.columns=["img_name"]
df['Index'] = df.index
print(df.head())

# Save new dataframe as csv

df.to_csv(file_path, index=False)

# Convert to json
list(df)

import csv
import json

csvfile = open(file_path, 'r')
jsonfile = open("/Volumes/Samsung_t3/project-repos/exercises/file.json", 'w')

fieldnames = ('img_name', 'Index')

reader = csv.DictReader(csvfile, fieldnames)
out = json.dumps( [row for row in reader])
jsonfile.write(out)






