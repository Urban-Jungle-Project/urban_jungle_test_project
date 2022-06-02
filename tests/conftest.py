from pytest import fixture
from libs.api.urban_jungle_api import UrbanJungleAPI
from libs.api.user_session import UserSession
from libs.utils.config_manager import EnvConfig, CommonConfig
from libs.utils.file_manager import FileManager
from libs.utils.misc import random_str
from tests.constants import EnvVariableNames, EnvVariableDefaultValues
import os

ALLURE_RESULTS_FOLDER = EnvVariableNames.ALLURE_RESULTS_FOLDER
ALLURE_RESULTS_FOLDER_DEFAULT = EnvVariableDefaultValues.ALLURE_RESULTS_FOLDER
ENVIRONMENT = EnvVariableNames.ENVIRONMENT


@fixture(scope="session")
def env_config():
    env_config = EnvConfig()
    return env_config


@fixture(scope="session")
def common_config():
    common_config = CommonConfig()
    return common_config


@fixture(scope="session")
def predefined_user(env_config, common_config):
    return {"username": common_config.user_name,
            "password": common_config.user_password,
            "email": common_config.user_email}


@fixture(scope="function")
def user_session(env_config, predefined_user):
    return UserSession(base_url=env_config.base_api_url, user=predefined_user)


@fixture(scope="session")
def urban_jungle_api(env_config, predefined_user):
    return UrbanJungleAPI(env_config.base_api_url, user=predefined_user)


@fixture(autouse=True, scope="session")
def clean_allure_dir():
    FileManager.clean_directory(os.environ.get(ALLURE_RESULTS_FOLDER,
                                               ALLURE_RESULTS_FOLDER_DEFAULT))


@fixture(autouse=True, scope="session")
def check_required_env_variables():
    for variable in [ENVIRONMENT]:
        if os.getenv(variable.upper()) is None:
            raise ValueError(f"Variable {variable} not specified.")


@fixture(scope="function")
def user_payload():
    def _generate_payload(**kwargs):
        user_random_str = random_str(6)
        user = {"password": kwargs.get('password', random_str(8)),
                "username": kwargs.get('username', f"user {user_random_str}"),
                "email": kwargs.get('email', f"user.test_{user_random_str}@gmail.com")}

        for field in ['username', 'email', 'password']:
            if user[field] is None:
                user.pop(field)
        return user

    return _generate_payload
