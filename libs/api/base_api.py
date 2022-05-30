import json

from requests import post, get, put, delete
from libs.api.common.custom_exceptions import MissingInputError
import base64


class BaseAPI:
    def __init__(self, base_url, **kwargs):
        self.base_url = base_url
        self.token = kwargs.get('token', None)
        self.user = kwargs.get('user', None)
        self.headers = {'Content-Type': 'application/json'}
        if self.token:
            self.headers['Authorization'] = f'Bearer {self.token}'
        elif self.user:
            basic_auth_str = base64.b64encode(f"{self.user['username']}:{self.user['password']}".
                                              encode('ascii')).decode('ascii')
            self.headers['Authorization'] = f'Basic {basic_auth_str}'
        elif kwargs.get('auth_header', None):
            self.headers['Authorization'] = kwargs.get('auth_header')
        else:
            raise MissingInputError('Please provide token or user authentication information.')

    def post(self, endpoint, data, empty_auth=False):
        response = post(f'{self.base_url}/{endpoint}',
                        headers=({'Content-Type': 'application/json'}if empty_auth else self.headers),
                        data=json.dumps(data))
        return response

    def get(self, endpoint):
        return get(f'{self.base_url}/{endpoint}', headers=self.headers)

    def put(self, endpoint, data):
        return put(f'{self.base_url}/{endpoint}', headers=self.headers, data=json.dumps(data))

    def delete(self, endpoint):
        return delete(f'{self.base_url}/{endpoint}', headers=self.headers)
