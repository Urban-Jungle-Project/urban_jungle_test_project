from libs.api.urban_jungle_api import UrbanJungleAPI
from libs.api.user_session import UserSession
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

