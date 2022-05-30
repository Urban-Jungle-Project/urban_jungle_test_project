import json

from libs.api.base_api import BaseAPI
from libs.utils.allure_wrapper import step
from libs.api.common.constants import ResourcePaths

PLANTS_PATH = ResourcePaths.PLANTS


class PlantsAPI(BaseAPI):

    @step(f'Send POST plant request')
    def post_plant(self, data):
        return self.post(f'{PLANTS_PATH}', data=data)

    @step(f'Send GET all plants request')
    def get_plants(self):
        return self.get(f'{PLANTS_PATH}')

    @step(f'Send GET plant by id request')
    def get_plant(self, plant_id):
        return self.get(f'{PLANTS_PATH}\{plant_id}')

    @step(f'Send PUT plant request')
    def put_plant(self, data):
        return self.put(f'{PLANTS_PATH}', data=data)

    @step(f'Send DELETE plant request')
    def delete_plant(self):
        return self.delete(f'{PLANTS_PATH}')
