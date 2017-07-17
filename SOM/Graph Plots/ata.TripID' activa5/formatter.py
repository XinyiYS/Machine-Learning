

          

names = ["locationAltitude","locationLongitude","locationVerticalAccuracy","locationHorizontalAccuracy","locationSpeed",
"locationHeadingTimestamp","locationHeadingY","locationTimestamp","locationLatitude","locationHeadingZ","locationMagneticHeading",
"locationHeadingX","locationCourse","locationTrueHeading","locationHeadingAccuracy"]

#define dict
gpsData = {}

#insert new pair
# gpsData[] = []

# print(len(name))
with open("gpsFields.txt", "w") as f: 
	for name in names:
		for i in range(51):
			f.write("data.sensor."+str(i)+".gpsData."+name+"\n") 
		# print("data.sensor."+str(i)+".gpsData"+name+"\n")
			i +=1