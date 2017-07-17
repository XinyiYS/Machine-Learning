import json
import numpy as np 
import pandas as pd
import sompy


class DPP_csv(object):
    '''
    A class designated to do reading and pre-processing of data, stored as numpy array in txt form
    '''

    # To check if the data has been loaded
    _loaded = False

    def __init__(self, data_dir, _loaded=False, data=None):

        self.data_dir = data_dir
        self._loaded = _loaded
        self.data = data

    def get_data(self, data_size=None, data_frac=0.2):
        if not self._loaded:
            self.df = pd.read_csv(self.data_dir)
            self._loaded = True

        df = pd.DataFrame.copy(self.df)
        if data_size == None:
            self.data_size = int((len(df)*data_frac))
            print(self.data_size)
        elif isinstance((data_size,int)):
            self.data_size = data_size
        else:
            print("Requested data size is not recognized, setting the data to be 10% of entire set")
            self.data_size = int(len(df)*data_frac)
        data_collected = False
        while not data_collected:
            chosen_attributes = self.choose_attributes()
            print(chosen_attributes)
            confirmation = input('Confirm that the listed attributes are correct (y/n): ').lower()
            if confirmation == 'y':
                print('Proceeding to data processing.')
                data_collected = True
                data_to_process = self.collect_data(df, chosen_attributes)
            elif confirmation == 'n':
                print()
                print('Please redo the choosing.')

        self.chosen_attributes = chosen_attributes
        self.data = data_to_process

        return data_to_process, chosen_attributes

    def choose_attributes(self):
        for i, key in enumerate(self.df.columns):
            print(i + 1, key)
        indices = input('Choose one or more indices of attributes of interest (separate by space): ').split()
        int_indices = []
        [int_indices.append(int(index)) for index in indices]
        chosen_attributes = []
        attributes = list(self.df)
        for i,attribute in enumerate(attributes):
            if i+1 in int_indices:
                chosen_attributes.append(attribute)
        print()
        return chosen_attributes

    def collect_data(self, data, chosen_attributes):
            temp_df = pd.DataFrame()
            for attribute in chosen_attributes:
                temp_df[attribute] = self.df[attribute]
            data_df = temp_df.sample(n=self.data_size)
            return data_df

