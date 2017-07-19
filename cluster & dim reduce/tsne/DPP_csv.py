import pandas as pd


class DPP_csv(object):
    '''
    A class designated to do reading and pre-processing of data, stored as numpy array in csv form
    Capable of aggregating consecutive points into one data point
    Capable of obtaining a random sample of the data points
    Capable of choosing a part of the data
    '''

    # To check if the data has been loaded
    _loaded = False

    def __init__(self, data_dir, _loaded=False, data=None):

        self.data_dir = data_dir
        self._loaded = _loaded
        self.data = data

    def get_data(self, sec_window=2, random_sampling=True, data_size=None, data_frac=0.1):
        if not self._loaded:
            self.df = pd.read_csv(self.data_dir)
            self._loaded = True

        self.window = sec_window * 10  # window is number of seconds
        # 10 is the frequency of data collection:
        # how many data points per second
        self.random_sampling = random_sampling
        if self.random_sampling:
            df = pd.DataFrame.copy(self.df)
            if data_size == None:
                self.data_size = int((len(df) * data_frac))
            elif isinstance((data_size, int)):
                self.data_size = data_size
            else:
                print("Requested data size is not recognized, setting the data to be 10% of entire set")
                self.data_size = int(len(df) * data_frac)

            self.data_frac = float(self.data_size / len(df))
        else:
            self.data_frac = 1
            self.data_size = len(self.df)

        data_collected = False
        while not data_collected:
            chosen_attributes = self.choose_attributes()
            print(chosen_attributes)
            confirmation = input('Confirm that the listed attributes are correct (y/n): ').lower()
            if confirmation == 'y':
                print('Proceeding to data collection.')
                orig_data, window_data = self.collect_data(chosen_attributes)
                data_collected = True
            elif confirmation == 'n':
                print()
                print('Please redo the choosing.')

        self.chosen_attributes = chosen_attributes
        self.orig_data = orig_data
        self.window_data = window_data

        return orig_data, window_data, chosen_attributes

    def choose_attributes(self):
        for i, key in enumerate(self.df.columns):
            print(i + 1, key)
        indices = input('Choose one or more indices of attributes of interest (separate by space): ').split()
        int_indices = []
        [int_indices.append(int(index)) for index in indices]
        chosen_attributes = []
        attributes = list(self.df)
        for i, attribute in enumerate(attributes):
            if i + 1 in int_indices:
                chosen_attributes.append(attribute)
        print()
        return chosen_attributes

    def collect_data(self, chosen_attributes):
        temp_df = pd.DataFrame()
        for attribute in chosen_attributes:
            temp_df[attribute] = self.df[attribute]

        window = self.window
        new_data = pd.DataFrame()
        row_name = []
        for attribute in chosen_attributes:
            row_name.extend(list([attribute + '_' + str(i) for i in range(window)]))
        for index, row in temp_df.iterrows():
            if index + window <= len(temp_df):
                row_data = []
                for attribute in chosen_attributes:
                    new_instance = temp_df[attribute].iloc[index:index + window]
                    row_data.extend(new_instance)
                row_df = pd.DataFrame(data=[row_data], index=[index], columns=row_name)
                new_data = pd.concat([new_data, row_df])
            else:
                break
        whole_window_combined_df = new_data.copy()

        if self.random_sampling:
            data_df = temp_df.sample(n=self.data_size)
            window_combined_df = whole_window_combined_df.sample(n=int(self.data_frac * len(whole_window_combined_df)))
        else:
            data_df = temp_df
            window_combined_df = whole_window_combined_df
        return data_df, window_combined_df
