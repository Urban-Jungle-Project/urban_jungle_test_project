from libs.api.urban_jungle_api import UrbanJungleAPI
from pytest import fixture


@fixture(scope="function")
def app_api_scope_function(env_config, common_config):
    api = UrbanJungleAPI(env_config.base_api_url, user={"username": common_config.user_name,
                                                        "password": common_config.user_password})
    return api

