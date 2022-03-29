from libs.api.auth_api import AuthAPI
from libs.api.users_api import UsersAPI


class UrbanJungleAPI:

    def __init__(self, base_url, user):
        self.auth = AuthAPI(base_url, user=user)
        self.token = self.auth.obtain_token()
        self.users = UsersAPI(base_url, token=self.token)