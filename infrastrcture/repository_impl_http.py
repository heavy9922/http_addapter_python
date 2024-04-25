import requests
from typing import Any
from app.repositories.base_http import BaseRepositoryHttp, DataType


class HttpRepository(BaseRepositoryHttp):
    def get_data_api(self, base_url: str, header=None, response_type=None) -> Any | None:
        response = requests.get(base_url)
        if response.status_code == 200 and response_type == 'json':
            return response.json()
        elif response.status_code == 200 and response_type == 'text':
            return response.text
        else:
            return None

    def create_data_api(self, base_url: str, body: DataType = None, header=None):
        response = requests.post(base_url, json=body)
        print(response)
        if response.status_code == 201:
            return response.json()
        else:
            return None

    def update_data_api(self, base_url: str, body: DataType = None, header=None) -> DataType:
        url = f"{base_url}"
        response = requests.put(url, json=body)
        if response.status_code == 200:
            return response.json()
        else:
            return None

    def delete_data_api(self, base_url: str, body: DataType = None, header=None):
        url = f"{base_url}"
        response = requests.delete(url)
        if response.status_code == 204 or response.status_code == 200:
            return True
        else:
            return False
