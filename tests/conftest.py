from pytest import fixture
from libs.api.urban_jungle_api import UrbanJungleAPI
from libs.utils.config_manager import EnvConfig, CommonConfig
from libs.utils.file_manager import FileManager
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
def app_api(env_config, common_config):
    api = UrbanJungleAPI(env_config.base_api_url, user={"username": common_config.user_name,
                                                        "password": common_config.user_password})
    return api


@fixture(autouse=True, scope="session")
def clean_allure_dir():
    FileManager.clean_directory(os.environ.get(ALLURE_RESULTS_FOLDER,
                                               ALLURE_RESULTS_FOLDER_DEFAULT))


@fixture(autouse=True, scope="session")
def check_required_env_variables():
    for variable in [ENVIRONMENT]:
        if os.getenv(variable.upper()) is None:
            raise ValueError(f"Variable {variable} not specified.")
