import os

from libs.utils.config_reader import ConfigReader
from tests.constants import ConfigFilePath, EnvVariableNames, EnvConfigName, CommonConfigName

ENVIRONMENT = EnvVariableNames.ENVIRONMENT


class EnvConfig:
    def __init__(self):
        self.config = ConfigReader(ConfigFilePath.ENV.format(os.environ.get(ENVIRONMENT)))
        self.base_api_url = self.config.read_section(EnvConfigName.BASE_API_URL)


class CommonConfig:
    def __init__(self):
        self.config = ConfigReader(ConfigFilePath.COMMON)
        self.user_name = self.config.read_section(CommonConfigName.USER_NAME)
        self.user_password = self.config.read_section(CommonConfigName.USER_PASSWORD)
        self.user_token_expiration_time = self.config.read_section(CommonConfigName.USER_TOKEN_EXPIRATION_TIME)
