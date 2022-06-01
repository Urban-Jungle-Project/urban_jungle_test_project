from libs.api.common.constants import ResponseCodes, ErrorMessages
from libs.utils.allure_wrapper import step
import pytest


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
