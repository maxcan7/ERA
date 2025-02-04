import yaml
import google.oauth2.credentials
from googleapiclient.discovery import build

from ERA.APIs import APIClient


class GoogleAPIClient(APIClient):

    def __init__(self, service, service_version, constants=None):
        creds = self.__load_credentials(constants)
        self.service = build(
            service, service_version, credentials=creds
        )

    def __load_credentials(self, constants=None):
        if constants:
            google_vars = constants['GOOGLE']
        else:
            with open('constants.yml', 'r') as f:
                google_vars = yaml.safe_load(f)['GOOGLE']
        refresh_token = google_vars['GOOGLE_API_REFRESH_TOKEN']
        token_uri = google_vars['GOOGLE_API_TOKEN_URI']
        client_id = google_vars['GOOGLE_API_CLIENT_ID']
        client_secret = google_vars['GOOGLE_API_CLIENT_SECRET']

        return google.oauth2.credentials.Credentials(
            token=None,
            refresh_token=refresh_token,
            token_uri=token_uri,
            client_id=client_id,
            client_secret=client_secret,
        )


class GoogleCivicClient(GoogleAPIClient):

    def __init__(self, constants=None):
        super(GoogleAPIClient, self)\
            .__init__('civicinfo', 'v2', constants=constants)

    def get(self, query, **kwargs):
        '''
        Due to issues with the Google API credentials, we
        decided not to pursue this dataset or other Google
        datasets for this project
        '''
        pass