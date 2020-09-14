import yaml
import pandas as pd

from ERA.offline_data_framework import OfflineData


class NYPDComplaints(OfflineData):

    def __init__(self, path=None, filetype=None):
        '''
        Class for loading of an offline dataset as a
        pandas dataframe. Requires either a file path as a
        keyword argument or a constants.yml with a COMPLAINTS
        key and PATH sub-key in the main directory, and a
        keyword argument filetype. Currently only supports csv.
        '''
        self.data = self.load(path=path, filetype=filetype)

    def load(self, path=None, filetype=None):
        if not path:
            with open('constants.yml', 'r') as f:
                path = yaml.safe_load(f)['COMPLAINTS']['PATH']
        formatter = {
            'csv': self.__load_csv(path=path)
        }
        return formatter[filetype]

    def __load_csv(self, path=None):
        with open(path, 'r') as f:
            data = pd.read_csv(f)
        return data
