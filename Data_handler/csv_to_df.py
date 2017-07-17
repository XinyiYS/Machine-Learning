import pandas as pd 
import csv
import numpy as np 
import ast

with open('dict.csv', 'r') as csv_file:
    reader = csv.reader(csv_file)
    data = dict(reader)

key = list(data.keys())
value1 = []
value2 = []
for k in key:
	value = ast.literal_eval(data[k])
	value1.append(value[0])
	value2.append(value[1])
df = pd.DataFrame({'asin':key,'description':value1,'categories':value2})
print(df.head())




