from libs.api.auth_api import AuthAPI
from libs.api.common.constants import ResponseCodes


def test_get_token_for_correct_credentials(env_config, common_config):
    auth_api = AuthAPI(env_config.base_api_url, user={"username": common_config.user_name,
                                                      "password": common_config.user_password})
    response = auth_api.get_token()
    assert response.status_code == ResponseCodes.SUCCESS
    response_json = response.json()
    assert response_json['token_type'] == 'Bearer'
    assert response_json['expires_in'] == 3600
    assert response_json['access_token'] is not None


def test_get_token_with_wrong_credentials(env_config, common_config):
    auth_api = AuthAPI(env_config.base_api_url,  user={"username": common_config.user_name,
                                                       "password": "wrong_password"})
    response = auth_api.get_token()
    assert response.status_code == ResponseCodes.UNAUTHORIZED
    response_json = response.json()
    assert response_json['error'] == 'Unauthorized'
    assert 'access_token' not in response_json.keys()


def test_get_token_with_wrong_header(env_config, common_config):
    auth_api = AuthAPI(env_config.base_api_url,  auth_header="Wrong header")
    response = auth_api.get_token()
    assert response.status_code == ResponseCodes.UNAUTHORIZED
    response_json = response.json()
    assert response_json['error'] == 'Unauthorized'
    assert 'access_token' not in response_json.keys()


def test_renew_token(app_api):
    original_token = app_api.users.token
    response = app_api.auth.get_token()
    assert response.status_code == ResponseCodes.SUCCESS
    response_json = response.json()
    assert response_json['access_token'] == original_token
    assert response_json['expires_in'] == 3600


def test_revoke_token(app_api):
    response = app_api.users.revoke_token()
    assert response.status_code == ResponseCodes.NO_CONTENT
    assert response.text == ''
    response = app_api.users.get_users()
    assert response.status_code == ResponseCodes.UNAUTHORIZED





