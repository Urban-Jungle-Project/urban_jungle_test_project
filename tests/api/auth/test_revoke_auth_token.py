from libs.api.common.constants import ResponseCodes
from libs.utils.allure_wrapper import step


def test_revoke_auth_token(app_api_scope_function):
    with step("Revoke user access token"):
        response = app_api_scope_function.user_session.revoke_token()
    with step("Assert NO_CONTENT response"):
        assert response.status_code == ResponseCodes.NO_CONTENT
        assert response.text == ''
    with step("Assert token is not valid anymore"):
        response = app_api_scope_function.users.get_users()
        assert response.status_code == ResponseCodes.UNAUTHORIZED



