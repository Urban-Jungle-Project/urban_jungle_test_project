from libs.api.common.constants import ResponseCodes
from libs.utils.allure_wrapper import step


def test_get_auth_token_with_correct_credentials(user_session, common_config):
    with step("Obtain user access token for correct credentials"):
        response = user_session.get_token()
    with step("Assert SUCCESS response code"):
        assert response.status_code == ResponseCodes.SUCCESS
    with step("Assert response json"):
        response_json = response.json()
        assert response_json['token_type'] == 'Bearer'
        assert response_json['expires_in'] == common_config.user_token_expiration_time
        assert response_json['access_token'] is not None
