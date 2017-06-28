import pymongo as pm 
import pprint
import json
import pickle
from pymongo import MongoClient

client = MongoClient('devsompo.nevaventures.com',27017)
db = client.sompo
collection = db.drive

queryResult = collection.find({'data.TripID':"Original_drive_data-Meghana's iPhone-activa5-1497356247.78158-0C3300C7-9FF1-4251-84DE-C7AD70DFA999"})

allFields = queryResult[0].keys()
allFieldsList = list(allFields)
dataFields = queryResult[0]['data'].keys()
dataFieldsList = list(dataFields)
sensorFields = queryResult[0]['data']['sensor'][0].keys()
sensorFieldsList = list(sensorFields)
specificDataFileds = queryResult[0]['data']['sensor'][0]

# print(allFieldsList,dataFieldsList,sensorFieldsList)

data ={}

for dataType in dataFieldsList:
	data[dataType] = {}


for sensorType in sensorFieldsList:
	data['sensor'][sensorType] = {}
	for specificData in queryResult[0]['data']['sensor'][0][sensorType]:
		data['sensor'][sensorType][specificData] = []

i=1
for post in queryResult:
	# print(i)
	i+=1
	data['PartID'] = i
	for sensorType in data['sensor'].keys():
		for specificData in data['sensor'][sensorType].keys():
			[data['sensor'][sensorType][specificData].append(post['data']['sensor'][i][sensorType][specificData]) for i in range(len(post['data']['sensor']))]
				



# import csv
# w = csv.writer(open("dataDict.csv", "w"))
# for key, val in data.items():
    # w.writerow([key, val])

import json
# dataStr = json.dumps(data)
with open('dataOut.txt','w') as j:
	json.dump(data,j)

# print(data)
