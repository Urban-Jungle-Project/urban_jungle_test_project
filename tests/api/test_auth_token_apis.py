import time

import pytest

from libs.api.urban_jungle_api import UrbanJungleAPI
from libs.api.user_session import UserSession
from libs.api.common.constants import ResponseCodes, TOKEN_EXPIRATION_TIME
from libs.api.users_api import UsersAPI
from libs.utils.allure_wrapper import step
from pytest import fixture


@fixture(scope="function")
def user_session(env_config, common_config):
    user_session = UserSession(base_url=env_config.base_api_url,
                               user={"username": common_config.user_name,
                                     "password": common_config.user_password})

    return user_session


@fixture(scope="function")
def app_api(env_config, common_config):
    api = UrbanJungleAPI(env_config.base_api_url, user={"username": common_config.user_name,
                                                        "password": common_config.user_password})
    return api


def test_get_token_for_correct_credentials(user_session):
    with step("Obtain user access token for correct credentials"):
        response = user_session.get_token()
    with step("Assert SUCCESS response code"):
        assert response.status_code == ResponseCodes.SUCCESS
    with step("Assert response json"):
        response_json = response.json()
        assert response_json['token_type'] == 'Bearer'
        assert response_json['expires_in'] == TOKEN_EXPIRATION_TIME
        assert response_json['access_token'] is not None


def test_get_token_with_wrong_credentials(env_config, common_config):
    with step("Obtain user access token for wrong credentials"):
        user_session = UserSession(base_url=env_config.base_api_url,
                                   user={"username": common_config.user_name,
                                         "password": "wrong_password"})
        response = user_session.get_token()
    with step("Assert UNAUTHORIZED response code"):
        assert response.status_code == ResponseCodes.UNAUTHORIZED
    with step("Assert response json"):
        response_json = response.json()
        assert response_json['error'] == 'Unauthorized'
        assert 'access_token' not in response_json.keys()


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


def test_renew_token(user_session):
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
        assert response_json['expires_in'] == TOKEN_EXPIRATION_TIME


def test_revoke_token(app_api):
    with step("Revoke user access token"):
        response = app_api.user_session.revoke_token()
    with step("Assert NO_CONTENT response"):
        assert response.status_code == ResponseCodes.NO_CONTENT
        assert response.text == ''
    with step("Assert token is not valid anymore"):
        response = app_api.users.get_users()
        assert response.status_code == ResponseCodes.UNAUTHORIZED


@pytest.mark.parametrize('headers', [{'Content-Type': 'application/json'},
                                     {'Content-Type': 'application/json',
                                      'Authorization': 'Bearer D5Oa7MX80+ou2AT1JGRY5r/X9CKkOt03'}],
                         ids=['missing authorization header ', 'wrong auth header'])
def test_auth_with_wrong_auth_header(env_config, headers):
    with step("Send request with empty auth token"):
        user_session = UserSession(base_url=env_config.base_api_url,
                                   headers=headers)
        users = UsersAPI(user_session=user_session)
        response = users.get_users()
    with step("Assert UNAUTHORIZED response code"):
        assert response.status_code == ResponseCodes.UNAUTHORIZED
    with step("Assert response json"):
        response_json = response.json()
        assert response_json['error'] == 'Unauthorized'
        assert 'access_token' not in response_json.keys()


@pytest.mark.timeconsuming
def test_auth_with_expired_token(app_api, common_config):
    with step("Renew auth token"):
        app_api.user_session.renew_token()
    with step("Wait for token expiration"):
        time.sleep(common_config.user_token_expiration_time)
    with step("Assert token has expired"):
        response = app_api.users.get_users()
        assert response.status_code == ResponseCodes.UNAUTHORIZED


