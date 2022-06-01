import time
import pytest

from libs.api.user_session import UserSession
from libs.api.common.constants import ResponseCodes
from libs.api.users_api import UsersAPI
from libs.utils.allure_wrapper import step


@pytest.mark.timeconsuming
def test_auth_with_expired_token(app_api, common_config):
    with step("Renew auth token"):
        app_api.user_session.renew_token()
    with step("Wait for token expiration"):
        time.sleep(common_config.user_token_expiration_time)
    with step("Assert token has expired"):
        response = app_api.users.get_users()
        assert response.status_code == ResponseCodes.UNAUTHORIZED


