import matplotlib as mpl
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cbook as cbook
import pandas as pd 
import json
with open('dataOut.txt') as fi:
    data = json.load(fi)


# locationAltitude = data['sensor']['gpsData']['locationAltitude']
# locationSpeed = data['sensor']['gpsData']['locationSpeed']

locationHeadingX = data['sensor']['gpsData']['locationHeadingX']
locationHeadingY = data['sensor']['gpsData']['locationHeadingY']
locationHeadingZ = data['sensor']['gpsData']['locationHeadingZ']
locationSpeed = data['sensor']['gpsData']['locationSpeed']
locationTimestamp = data['sensor']['gpsData']['locationTimestamp']
duration = locationTimestamp[1112] - locationTimestamp[0]

accelerometerAccelerationX = data['sensor']['accelerometerData']['accelerometerAccelerationX']
accelerometerAccelerationY = data['sensor']['accelerometerData']['accelerometerAccelerationY']
accelerometerAccelerationZ = data['sensor']['accelerometerData']['accelerometerAccelerationZ']
accelerometerTimestamp = data['sensor']['accelerometerData']['accelerometerTimestamp']

locationHeadingTimestamp = data['sensor']['gpsData']['locationHeadingTimestamp']
duration = locationHeadingTimestamp[1112] - locationHeadingTimestamp[0]


gyroRotationX = data['sensor']['gyroData']['gyroRotationX']
gyroRotationY = data['sensor']['gyroData']['gyroRotationY']
gyroRotationZ = data['sensor']['gyroData']['gyroRotationZ']
motionRotationRateX= data['sensor']['gyroData']['motionRotationRateX']
motionRotationRateY= data['sensor']['gyroData']['motionRotationRateY']
motionRotationRateZ= data['sensor']['gyroData']['motionRotationRateZ']
gyroTimestamp =   data['sensor']['gyroData']['gyroTimestamp']
duration = gyroTimestamp[1112] - gyroTimestamp[0]
print(duration)

# plt.plot(x1, y1, x2, y2, marker = 'o')

plt.xlim([0.0,duration])
# plt.plot(locationHeadingX)
# plt.plot(locationHeadingY)
# plt.plot(locationHeadingZ)

# accelerationPoints 
x1 , y1 = [22,22],[-3,1]
x2 , y2 = [67 ,67 ],[-3,1]
x3 , y3 = [74,74],[-3,1]

# breakPoints
# x1 , y1 = [37,37],[-3,1]
# x2 , y2 = [72,72 ],[-3,1]
# x3 , y3 = [76,76],[-3,1]

# turnPoints
# x1 , y1 = [42,42],[-3,1]
# x2 , y2 = [80,80],[-3,1]

#speedbreaker
# x1 , y1 = [78,78],[-3,1]
# x2 , y2 = [88,88],[-3,1]

#stop
x1 , y1 = [90,90],[-3,1]

plt.plot(x1,y1, 'r:',linewidth = 1)
plt.plot(x2,y2, 'r:',linewidth = 1)
plt.plot(x3,y3, 'r:',linewidth = 1)

# plt.plot(accelerometerAccelerationX)
# plt.plot(accelerometerAccelerationY)
# plt.plot(accelerometerAccelerationZ)


# plt.plot(motionRotationRateX)
# plt.plot(motionRotationRateY)
# plt.plot(motionRotationRateZ)

plt.plot(locationSpeed)

plt.show()