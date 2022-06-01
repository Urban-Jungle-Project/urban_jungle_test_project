from libs.api.common.constants import ResponseCodes, ErrorMessages
from libs.utils.allure_wrapper import step
import pytest


def test_sign_up_new_user_positive(app_api, user_payload):
    with step("Send sign up new user request"):
        response = app_api.users.post_user(data=user_payload())
    with step("Assert CREATED response code"):
        assert response.status_code == ResponseCodes.CREATED
    with step("Assert response json"):
        response_json = response.json()
        assert response_json['id'] is not None


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


@pytest.mark.parametrize('username', [(None, ErrorMessages.REQUIRED_USER_PARAMETERS),
                                      ('', ErrorMessages.REQUIRED_USER_PARAMETERS_USER_RULES)],
                         ids=['missing username', 'empty string'])
def test_sign_up_new_user_wrong_username(username, app_api, user_payload):
    username_str = username[0]
    error_message = username[1]

    with step("Send sign up new user request"):
        response = app_api.users.post_user(data=user_payload(username=username_str))
    with step("Assert BAD_REQUEST response code"):
        assert response.status_code == ResponseCodes.BAD_REQUEST
    with step("Assert response error message"):
        response_json = response.json()
        assert response_json['message'] == error_message


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

