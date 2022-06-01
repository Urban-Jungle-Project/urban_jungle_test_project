from libs.api.common.constants import ResponseCodes, ErrorMessages
from libs.utils.allure_wrapper import step
import pytest


@pytest.mark.parametrize('password', [(None, ErrorMessages.REQUIRED_USER_PARAMETERS),
                                      ('', ErrorMessages.REQUIRED_USER_PARAMETERS_PASSWORD_RULES),
                                      ('1234567', ErrorMessages.REQUIRED_USER_PARAMETERS_PASSWORD_RULES)],
                         ids=['missing password', 'empty string', '7 chars'])
def test_sign_up_new_user_wrong_password(password, app_api, user_payload):
    password_str = password[0]
    error_message = password[1]

    with step("Send sign up new user request"):
        response = app_api.users.post_user(data=user_payload(password=password_str))
    with step("Assert BAD_REQUEST response code"):
        assert response.status_code == ResponseCodes.BAD_REQUEST
    with step("Assert response error message"):
        response_json = response.json()
        assert response_json['message'] == error_message

