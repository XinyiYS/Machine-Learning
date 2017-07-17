import json
import numpy as np 
import pandas as pd
import sompy


class DPP(object):
    '''
    A class designated to do reading and pre-processing of data, stored as numpy array in txt form
    '''

    # To check if the data has been loaded
    _loaded = False

    def __init__(self, data_dir, _loaded=False, data=None):

        self.data_dir = data_dir
        self._loaded = _loaded
        self.data = data

    def get_data(self, data_size=None, data_frac=0.1):
        if not self._loaded:
            with open(self.data_dir) as fi:
            # with open('dataOut.txt') as fi:
                self.data_dict = json.load(fi)
            self._loaded = True

        data = self.data_dict
        if data_size == None:
            self.data_size = (len(data)*data_frac)
            print(len(data))
            print(self.data_size)
        elif isinstance((data_size,int)):
            self.data_size = data_size
        else:
            print("Requested data size is not recognized, setting the data to be 10% of entire set")
            self.data_size = int(len(data)*data_frac)
        data_processed = False
        while not data_processed:
            chosen_sensors = self.choose_sensors()
            chosen_attributes = {}
            for chosenSensor in chosen_sensors:
                chosen_attributes[chosenSensor] = self.choose_attributes(chosenSensor)
            print(list(chosen_attributes.values()))
            confirmation = input('Confirm that the listed attributes are correct (y/n): ').lower()
            if confirmation == 'y':
                print('Proceeding to data processing.')
                data_processed = True
                data_to_process = self.process_data(data, chosen_attributes)
            elif confirmation == 'n':
                print()
                print('Please redo the choosing.')

        self.chosen_attributes = chosen_attributes
        self.data = data_to_process

        return data_to_process, chosen_attributes

    def choose_sensors(self):
            sensor_list = list(self.data_dict['sensor'].keys())
            for i,key in enumerate(sensor_list):
                print(i+1,key)
            indices = input('Choose one or more indices of sensors of interest (separate by space): ').split()
            int_indices = []
            [int_indices.append(int(index)) for index in indices]
            chosen_sensors = []
            [chosen_sensors.append(sensor_list[index - 1]) for index in int_indices]
            # [print(sensorList[index-1]) for index in intIndices]
            print()
            return chosen_sensors

    def choose_attributes(self, sensor):
            attributes_list = list(self.data_dict['sensor'][sensor])
            print(sensor)
            for i, key in enumerate(attributes_list):
                print(i+1,key)
            indices = input('Choose one or more indices of attributes of interest (separate by space): ').split()
            int_indices = []
            [int_indices.append(int(index)) for index in indices]
            chosen_attributes = []
            [chosen_attributes.append(attributes_list[index - 1]) for index in int_indices]
            print()
            return chosen_attributes

    def process_data(self, data, chosen_attributes):
            df = self.collect_data(data, chosen_attributes)
            data_to_process = np.array(df)
            return data_to_process

    def collect_data(self, data, chosen_attributes):
            df = {}
            for sensor, attributes in chosen_attributes.items():
                for attribute in attributes:
                    df[attribute] = data['sensor'][sensor][attribute]
            df = pd.DataFrame(df)
            data_df = df.sample(n=self.data_size)
            return data_df

