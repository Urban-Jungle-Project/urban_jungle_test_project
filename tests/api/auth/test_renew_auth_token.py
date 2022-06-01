from libs.api.common.constants import ResponseCodes
from libs.utils.allure_wrapper import step


def test_renew_auth_token(user_session, common_config):
    with step("Obtain new user access token"):
        user_session.get_token()
        original_token = user_session.token
    with step("Renew user access token"):
        response = user_session.get_token()
    with step("Assert SUCCESS response code"):
        assert response.status_code == ResponseCodes.SUCCESS
    with step("Assert response json"):
        response_json = response.json()
        assert response_json['access_token'] != original_token
        assert response_json['expires_in'] == common_config.user_token_expiration_time
