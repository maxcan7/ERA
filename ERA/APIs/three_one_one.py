import yaml
import pandas as pd
from sodapy import Socrata


class NYCODAPIClient(APIClient):

    def __init__(self):
        creds = self.__load_credentials()
        self.service = Socrata(
            "data.cityofnewyork.us",
            creds['APP_TOKEN'],
            userame=creds['USERNAME'],
            password=creds['PASSWORD']
        )

    def __load_credentials(self):
        with open('constants.yml', 'r') as f:
            return yaml.safe_load(f)['NYCOD']
