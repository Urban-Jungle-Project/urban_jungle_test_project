from libs.api.auth_api import AuthAPI
from libs.api.common.constants import ResponseCodes
from libs.utils.allure_wrapper import step


def test_get_token_for_correct_credentials(env_config, common_config):
    with step("Obtain user access token for correct credentials"):
        auth_api = AuthAPI(env_config.base_api_url, user={"username": common_config.user_name,
                                                          "password": common_config.user_password})
        response = auth_api.get_token()
    with step("Assert SUCCESS response code"):
        assert response.status_code == ResponseCodes.SUCCESS
    with step("Assert response json"):
        response_json = response.json()
        assert response_json['token_type'] == 'Bearer'
        assert response_json['expires_in'] == 3600
        assert response_json['access_token'] is not None


def test_get_token_with_wrong_credentials(env_config, common_config):
    with step("Obtain user access token for wrong credentials"):
        auth_api = AuthAPI(env_config.base_api_url,  user={"username": common_config.user_name,
                                                           "password": "wrong_password"})
        response = auth_api.get_token()
    with step("Assert UNAUTHORIZED response code"):
        assert response.status_code == ResponseCodes.UNAUTHORIZED
    with step("Assert response json"):
        response_json = response.json()
        assert response_json['error'] == 'Unauthorized'
        assert 'access_token' not in response_json.keys()


def test_get_token_with_wrong_header(env_config, common_config):
    with step("Obtain user access token for wrong authorization header"):
        auth_api = AuthAPI(env_config.base_api_url,  auth_header="Wrong header")
        response = auth_api.get_token()
    with step("Assert UNAUTHORIZED response code"):
        assert response.status_code == ResponseCodes.UNAUTHORIZED
    with step("Assert response json"):
        response_json = response.json()
        assert response_json['error'] == 'Unauthorized'
        assert 'access_token' not in response_json.keys()


def test_renew_token(app_api):
    with step("Renew user access token"):
        original_token = app_api.users.token
        response = app_api.auth.get_token()
    with step("Assert SUCCESS response code"):
        assert response.status_code == ResponseCodes.SUCCESS
    with step("Assert response json"):
        response_json = response.json()
        assert response_json['access_token'] == original_token
        assert response_json['expires_in'] == 3600


def test_revoke_token(app_api):
    with step("Revoke user access token"):
        response = app_api.users.revoke_token()
    with step("Assert NO_CONTENT response"):
        assert response.status_code == ResponseCodes.NO_CONTENT
        assert response.text == ''
    with step("Assert token is not valid anymore"):
        response = app_api.users.get_users()
        assert response.status_code == ResponseCodes.UNAUTHORIZED





