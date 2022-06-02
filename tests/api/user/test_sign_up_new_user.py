from libs.api.common.constants import ResponseCodes
from libs.api.user_session import UserSession
from libs.api.users_api import UsersAPI
from libs.utils.allure_wrapper import step


def test_sign_up_new_user(env_config, user_payload):

    with step("Sign up new user"):
        user_data = user_payload()
        user_session = UserSession(base_url=env_config.base_api_url, user=user_data)
        users = UsersAPI(user_session=user_session)
        response_json = users.sign_up_new_user(data=user_data)
    with step("Assert response json"):
        user_id = response_json['id']
        assert user_id is not None
    with step("Get user by id"):
        user_session.obtain_token()
        response = users.get_user(user_id=user_id)
    with step("Assert SUCCESS response code"):
        assert response.status_code == ResponseCodes.SUCCESS
    with step("Assert response json"):
        response_json = response.json()
        assert response_json['id'] == user_id
        assert response_json['username'] == user_data['username']
        assert response_json['email'] == user_data['email']
        assert response_json['about_me'] is None
