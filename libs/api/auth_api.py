from libs.api.base_api import BaseAPI
from libs.api.common.constants import ResourcePaths
from libs.utils.allure_wrapper import step

TOKENS_PATH = ResourcePaths.TOKENS


class AuthAPI(BaseAPI):

    @step(f'Send GET token request')
    def get_token(self):
        return self.post(f'{TOKENS_PATH}', None)

    @step(f'Obtain new user access token')
    def obtain_token(self):
        response = self.get_token()
        return response.json()['access_token']
