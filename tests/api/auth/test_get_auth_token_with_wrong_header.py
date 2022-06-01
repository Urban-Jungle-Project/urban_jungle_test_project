from libs.api.user_session import UserSession
from libs.api.common.constants import ResponseCodes
from libs.utils.allure_wrapper import step


def test_get_token_with_wrong_header(env_config, common_config):
    with step("Obtain user access token for wrong authorization header"):
        user_session = UserSession(base_url=env_config.base_api_url,
                                   headers="Wrong header")
        response = user_session.get_token()
    with step("Assert UNAUTHORIZED response code"):
        assert response.status_code == ResponseCodes.UNAUTHORIZED
    with step("Assert response json"):
        response_json = response.json()
        assert response_json['error'] == 'Unauthorized'
        assert 'access_token' not in response_json.keys()
