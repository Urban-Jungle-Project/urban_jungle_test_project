from libs.api.user_session import UserSession
from libs.api.users_api import UsersAPI
from libs.utils.allure_wrapper import step


def test_update_user(env_config, user_payload):

    with step("Sign up & authorize new user"):
        user_data = user_payload()
        user_session = UserSession(base_url=env_config.base_api_url, user=user_data)
        users = UsersAPI(user_session=user_session)
        original_user = users.sign_up_new_user(data=user_data)
        user_session.obtain_token()
    with step("Update user"):
        updated_user_data = user_payload()
        updated_user = users.update_user(user_id=original_user['id'], data=updated_user_data)
    with step("Verify user updated"):
        assert updated_user['id'] == original_user['id']
        assert updated_user['username'] == updated_user_data['username']
        assert updated_user['email'] == updated_user_data['email']

