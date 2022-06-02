from libs.api.common.constants import ResponseCodes
from libs.api.user_session import UserSession
from libs.api.users_api import UsersAPI
from libs.utils.allure_wrapper import step


def test_sign_up_new_user(env_config, user_payload):

    with step("Send sign up new user request"):
        user_data = user_payload()
        user_session = UserSession(base_url=env_config.base_api_url, user=user_data)
        users = UsersAPI(user_session=user_session)
        response = users.post_user(data=user_data)
    with step("Assert CREATED response code"):
        assert response.status_code == ResponseCodes.CREATED
    with step("Assert response json"):
        response_json = response.json()
        assert response_json['id'] is not None

