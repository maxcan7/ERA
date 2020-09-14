import yaml
from sodapy import Socrata

from ERA.APIs import APIClient


class NYCODAPIClient(APIClient):

    def __init__(self, constants=None):
        creds = self.__load_credentials(constants)
        self.DATA_URL = creds['DATA_URL']
        self.DATASET = creds['DATASET']
        self.service = Socrata(
            self.DATA_URL,
            creds['APP_TOKEN'],
            username=creds['USERNAME'],
            password=creds['PASSWORD']
        )
        self.service.timeout = 60

    def __load_credentials(self, constants=None):
        if constants:
            return constants['NYCOD']
        with open('constants.yml', 'r') as f:
            return yaml.safe_load(f)['NYCOD']

    def get(self, query, **kwargs):
        return self.service.get(query, **kwargs)
