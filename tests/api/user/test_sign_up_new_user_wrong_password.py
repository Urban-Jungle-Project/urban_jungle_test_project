from libs.api.common.constants import ResponseCodes, ErrorMessages
from libs.api.user_session import UserSession
from libs.api.users_api import UsersAPI
from libs.utils.allure_wrapper import step
import pytest


@pytest.mark.parametrize('password', [(None, ErrorMessages.REQUIRED_USER_PARAMETERS),
                                      ('', ErrorMessages.REQUIRED_USER_PARAMETERS_PASSWORD_RULES),
                                      ('1234567', ErrorMessages.REQUIRED_USER_PARAMETERS_PASSWORD_RULES)],
                         ids=['missing password', 'empty string', '7 chars'])
def test_sign_up_new_user_wrong_password(password, env_config, user_payload):

    with step("Send sign up new user request"):
        user_data = user_payload(password=password[0])
        user_session = UserSession(base_url=env_config.base_api_url, user=user_data)
        users = UsersAPI(user_session=user_session)
        response = users.post_user(data=user_data)
    with step("Assert BAD_REQUEST response code"):
        assert response.status_code == ResponseCodes.BAD_REQUEST
    with step("Assert response error message"):
        response_json = response.json()
        error_message = password[1]
        assert response_json['message'] == error_message

