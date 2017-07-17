import json,ast,csv
import pandas as pd 
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
df = pd.DataFrame(dataList,columns=keys)


fp.close()

# with open('dict.csv', 'w') as csv_file:
#     writer = csv.writer(csv_file)
#     for key, value in data.items():
#        writer.writerow([key, value])

# with open('dict.csv', 'r') as csv_file:
    # reader = csv.reader(csv_file)
    # data = dict(reader)
