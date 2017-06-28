import matplotlib as mpl
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cbook as cbook
import pandas as pd 

df = pd.read_csv("gpsout.csv")
print(len(df))


higherFields  = ["gpsData","metaData","accelerometerData","gravityData","magnetometerData","gyroData","orientationData","miscellenousData"]

gpsFields = ["locationAltitude","locationLongitude","locationVerticalAccuracy","locationHorizontalAccuracy","locationSpeed",
"locationHeadingTimestamp","locationHeadingY","locationTimestamp","locationLatitude","locationHeadingZ","locationMagneticHeading",
"locationHeadingX","locationCourse","locationTrueHeading","locationHeadingAccuracy"]

metaFields = []

acceFeilds = []

gravFields = []

mangeFields = []

gyroFields = []

orienFields = []

miscellFields = []

# print(len(currList))

# define dict
Data = {}
gpsData = {}
Data['gpsData'] = gpsData 

for i in range(len(gpsFields)):
	currList = df.iloc[i*(22)]

	'''
	len of each particular field is 22 	
	'''
	for ii in range(22-1):
		currList = currList.append(df.iloc[i*22+ii+1])

	#insert new pair
	gpsData[gpsFields[i]] = [currList]
pring(currList.head())
