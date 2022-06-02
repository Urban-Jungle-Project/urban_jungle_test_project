from libs.api.common.constants import ResponseCodes, ErrorMessages
from libs.api.user_session import UserSession
from libs.api.users_api import UsersAPI
from libs.utils.allure_wrapper import step
import pytest


@pytest.mark.parametrize('email', [(None, ErrorMessages.REQUIRED_USER_PARAMETERS),
                                   ('', ErrorMessages.REQUIRED_USER_PARAMETERS_VALID_EMAIL_ADDRESS),
                                   ('badformat@gmailcom', ErrorMessages.REQUIRED_USER_PARAMETERS_VALID_EMAIL_ADDRESS)],
                         ids=['missing username', 'empty string', 'wrong format'])
def test_sign_up_new_user_wrong_email(email, env_config, user_payload):

    with step("Send sign up new user request"):
        user_data = user_payload(email=email[0])
        user_session = UserSession(base_url=env_config.base_api_url, user=user_data)
        users = UsersAPI(user_session=user_session)
        response = users.post_user(data=user_data)
    with step("Assert BAD_REQUEST response code"):
        assert response.status_code == ResponseCodes.BAD_REQUEST
    with step("Assert response error message"):
        response_json = response.json()
        error_message = email[1]
        assert response_json['message'] == error_message

