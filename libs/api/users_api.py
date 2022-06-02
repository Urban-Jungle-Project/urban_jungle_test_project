from libs.api.base_api import BaseAPI
from libs.api.common.constants import ResourcePaths
from libs.utils.allure_wrapper import step

USERS_PATH = ResourcePaths.USERS
TOKENS_PATH = ResourcePaths.TOKENS


class UsersAPI(BaseAPI):

    @step(f'Send POST user request')
    def post_user(self, data):
        return self.post(f'{USERS_PATH}', data=data)

    @step(f'Send GET all users request')
    def get_users(self):
        return self.get(f'{USERS_PATH}')

    @step(f'Send GET user by id request')
    def get_user(self, user_id):
        return self.get(f'{USERS_PATH}\{user_id}')

    @step(f'Send PUT user request')
    def put_user(self, data):
        return self.put(f'{USERS_PATH}', data=data)

