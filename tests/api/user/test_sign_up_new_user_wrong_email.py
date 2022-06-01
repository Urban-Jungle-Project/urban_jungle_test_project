from libs.api.common.constants import ResponseCodes, ErrorMessages
from libs.utils.allure_wrapper import step
import pytest


@pytest.mark.parametrize('email', [(None, ErrorMessages.REQUIRED_USER_PARAMETERS),
                                   ('', ErrorMessages.REQUIRED_USER_PARAMETERS_VALID_EMAIL_ADDRESS),
                                   ('badformat@gmailcom', ErrorMessages.REQUIRED_USER_PARAMETERS_VALID_EMAIL_ADDRESS)],
                         ids=['missing username', 'empty string', 'wrong format'])
def test_sign_up_new_user_wrong_email(email, app_api, user_payload):
    email_str = email[0]
    error_message = email[1]

    with step("Send sign up new user request"):
        response = app_api.users.post_user(data=user_payload(email=email_str))
    with step("Assert BAD_REQUEST response code"):
        assert response.status_code == ResponseCodes.BAD_REQUEST
    with step("Assert response error message"):
        response_json = response.json()
        assert response_json['message'] == error_message

