import yaml
from sodapy import Socrata

from ERA.APIs import APIClient


class NYCODAPIClient(APIClient):

    def __init__(self, constants=None, path=None):
        '''
        API Client for NYC Open Data. Create an instance with
        one of the following:

        constants: A dictionary with a key 'NYCOD' and
        sub-dictionary with keys DATA_URL, DATASET, APP_TOKEN,
        USERNAME, and PASSWORD.

        path: A path to a constants.yml file with the same
        fields as references above.
        '''
        creds = self.__load_credentials(constants=constants, path=path)
        self.DATA_URL = creds['DATA_URL']
        self.DATASET = creds['DATASET']
        self.service = Socrata(
            self.DATA_URL,
            creds['APP_TOKEN'],
            username=creds['USERNAME'],
            password=creds['PASSWORD']
        )
        self.service.timeout = 60

    def __load_credentials(self, constants=None, path=None):
        if constants:
            return constants['NYCOD']
        with open(path, 'r') as f:
            creds = yaml.safe_load(f)['NYCOD']
            return creds

    def get(self, query, **kwargs):
        '''
        Query the NYCOD API. The dataset can be used as a
        SELECT * query, with keyword argument limit=x. Also
        supports more sophisticated queries using
        dicts / JSON blob
        '''
        return self.service.get(query, **kwargs)
