import json,ast,csv
import pandas as pd 

filename = 'meta_Kindle_Store.json'
fp = open(filename)
keys = ['asin','description','categories']

values0 = []
values1 = []
values2 = []
for i, line in enumerate(fp): 
	line = ast.literal_eval(line)
	values0.append(line['asin'])

	if 'description' in line:
		value1 = line['description']
	else:
		value1 = 0
	if 'categories' in line:
		value2 = line['categories']
	else:
		value2 = 0 
	values1.append(value1)
	values2.append(value2)

	# remove the if and break to load all data
	if i == 2000:
		break
fp.close()
df = pd.DataFrame({keys[0]:values0,keys[1]:values1,keys[2]:values2},columns=keys)

