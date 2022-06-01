import json
from requests import post, get, put, delete


class BaseAPI:
    def __init__(self, **kwargs):
        self.user_session = kwargs.get('user_session', None)
        self.base_url = self.user_session.base_url
        self.headers = self.user_session.headers

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
