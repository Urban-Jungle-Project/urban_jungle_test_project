import yaml


class ConfigReader:
    def __init__(self, config_file_path):
       self._config_file_path = config_file_path
       self.config = self.read_yml(self._config_file_path)

    @staticmethod
    def read_yml(file_path):
        with open(file_path, 'r') as ymlfile:
            config = yaml.load(ymlfile, Loader=yaml.FullLoader)
        return config

    def read_section(self, section_name):
        return self.config.get(section_name)
