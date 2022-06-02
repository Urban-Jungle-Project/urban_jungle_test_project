import time
import pytest

from libs.api.common.constants import ResponseCodes
from libs.utils.allure_wrapper import step


@pytest.mark.timeconsuming
def test_auth_with_expired_token(app_api_scope_function, common_config):
    with step("Renew auth token"):
        app_api_scope_function.user_session.renew_token()
    with step("Wait for token expiration"):
        time.sleep(common_config.user_token_expiration_time)
    with step("Assert token has expired"):
        response = app_api_scope_function.users.get_users()
        assert response.status_code == ResponseCodes.UNAUTHORIZED


