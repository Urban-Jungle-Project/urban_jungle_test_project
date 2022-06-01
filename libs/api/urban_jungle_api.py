from libs.api.user_session import UserSession
from libs.api.users_api import UsersAPI


class UrbanJungleAPI:

    def __init__(self, base_url, user):
        self.user_session = UserSession(base_url, user=user)
        self.user_session.obtain_token()
        self.users = UsersAPI(user_session=self.user_session)

