import yaml
import pandas as pd


class NYPDComplaints:
    def __init__(self):
        with open('constants.yml', 'r') as f:
            complaints = yaml.safe_load(f)['COMPLAINTS']
        self.data = pd.read_csv(complaints['PATH'])
