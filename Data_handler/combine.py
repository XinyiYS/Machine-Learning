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
meta_df = pd.DataFrame({keys[0]:values0,keys[1]:values1,keys[2]:values2},columns=keys)


# Same from store_to_df.py: create a df from the store file, only 20000 instances
filename = 'Kindle_Store_5 (1).json'
fp = open(filename)
keys = []
dataList = []
# Append the data to a list
for i, line in enumerate(fp): 
	line = ast.literal_eval(line)
	keys = list(line.keys())
	dataList.append(list(line.values()))
	
	# delete the if-break to load the entire data set
	if i==2000:
		break
# Create the datafrom from the list
store_df = pd.DataFrame(dataList,columns=keys)
fp.close()

combined_df = pd.merge(meta_df,store_df,on='asin')
print(combined_df.head())


filename = 'combined_2000.csv'
combined_df.to_csv(filename, index=False, encoding='utf-8')


