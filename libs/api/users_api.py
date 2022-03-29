from libs.api.base_api import BaseAPI
from libs.api.common.constants import ResourcePaths
from libs.utils.allure_wrapper import step

USERS_PATH = ResourcePaths.USERS
TOKENS_PATH = ResourcePaths.TOKENS


class UsersAPI(BaseAPI):

    @step(f'GET users')
    def get_users(self):
        return self.get(f'{USERS_PATH}')

    @step(f'DELETE token')
    def revoke_token(self):
        return self.delete(f'{TOKENS_PATH}')
