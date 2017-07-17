import json

import numpy as np
import pandas as pd

# dpp = DPP.DPP(data_dir='dataOut.txt')
# data, chosen_attributes = dpp.get_data(data_frac= 0.3)
with open('dataOut.txt') as fi:
    data_dict = json.load(fi)

headers = []
dataList = []
for key in data_dict['sensor'].keys():
    subHeaders  = list((data_dict['sensor'][key].keys()))
    headers+=subHeaders
    for sub in subHeaders:
        dataList.append(data_dict['sensor'][key][sub])

dataList = np.array(dataList)
dataList = dataList.T
df = pd.DataFrame(dataList, columns=headers)

filename = 'dataOut.csv'
df.to_csv(filename, index=False, encoding='utf-8')
print('done')