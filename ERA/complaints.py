import yaml
import pandas as pd


class NYPDComplaints:
    def __init__(self, dbfs_path=None):
        if dbfs_path:
            with open(dbfs_path,'r') as f:
                self.data = pd.read_csv(f)
            return
        with open('constants.yml', 'r') as f:
            complaints = yaml.safe_load(f)['COMPLAINTS']
        self.data = pd.read_csv(complaints['PATH'])
