import pytest

from libs.api.user_session import UserSession
from libs.api.common.constants import ResponseCodes
from libs.api.users_api import UsersAPI
from libs.utils.allure_wrapper import step


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



