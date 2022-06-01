import base64

import requests

from libs.api.common.constants import ResourcePaths, ResponseCodes
from libs.utils.allure_wrapper import step

TOKENS_PATH = ResourcePaths.TOKENS


class UserSession:

    def __init__(self, base_url, **kwargs):
        self.base_url = base_url
        self.token = kwargs.get('token', None)
        self.user = kwargs.get('user', None)
        self.headers = kwargs.get('headers', {'Content-Type': 'application/json'})

    @step(f'Send GET token request')
    def get_token(self):
        if self.user:
            basic_auth_str = base64.b64encode(f"{self.user['username']}:{self.user['password']}".
                                          encode('ascii')).decode('ascii')
            headers = {'Authorization': f'Basic {basic_auth_str}'}
        else:
            headers = {'Authorization': self.headers}
        return requests.post(f'{self.base_url}/{TOKENS_PATH}', headers=headers)

    @step(f'Obtain new user access token')
    def obtain_token(self):
        response = self.get_token()
        assert response.status_code == ResponseCodes.SUCCESS
        token = response.json()['access_token']
        self.token = token
        self.headers['Authorization'] = f'Bearer {self.token}'
        return token

    @step(f'Send DELETE token request')
    def revoke_token(self):
        return requests.delete(f'{self.base_url}/{TOKENS_PATH}', headers=self.headers)

    @step(f'Renew user access token')
    def renew_token(self):
        return self.obtain_token()