from libs.api.common.constants import ResponseCodes
from libs.utils.allure_wrapper import step


def test_sign_up_new_user(app_api, user_payload):
    with step("Send sign up new user request"):
        response = app_api.users.post_user(data=user_payload())
    with step("Assert CREATED response code"):
        assert response.status_code == ResponseCodes.CREATED
    with step("Assert response json"):
        response_json = response.json()
        assert response_json['id'] is not None

