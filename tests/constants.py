from enum import Enum


class EnvVariableNames(str, Enum):
    ENVIRONMENT = 'ENVIRONMENT'
    ALLURE_RESULTS_FOLDER = 'ALLURE_RESULTS_FOLDER'


class EnvVariableDefaultValues(str, Enum):
    ALLURE_RESULTS_FOLDER = 'allure_results'


class EnvConfigName(str, Enum):
    BASE_API_URL = 'base_api_url'


class CommonConfigName(str, Enum):
    USER_NAME = 'user_name'
    USER_PASSWORD = 'user_password'
    USER_EMAIL = 'user_email'
    USER_TOKEN_EXPIRATION_TIME = 'user_token_expiration_time'


class ConfigFilePath(str, Enum):
    ENV = "config/{}_env.yml"
    COMMON = "config/common.yml"

