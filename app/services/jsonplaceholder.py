from app.repositories.base_http import BaseRepositoryHttp


class JsonPlaceholderServices:
    def __init__(self, http_repo: BaseRepositoryHttp):
        self.http_repo = http_repo
        self.url = 'https://jsonplaceholder.typicode.com'

    def create_json_placeholder(self, data: dict) -> dict:
        url = f'{self.url}/posts'
        return self.http_repo.create_data_api(base_url=url, body=data)

    def get_json_placeholder(self):
        url = f'{self.url}/posts'
        return self.http_repo.get_data_api(base_url=url, response_type='json')

    def get_json_placeholder_by_id(self, id: str):
        url = f'{self.url}/posts/{id}'
        return self.http_repo.get_data_api(base_url=url, response_type='json')

    def update_json_placeholder(self, id: str, data: dict) -> dict:
        url = f'{self.url}/posts/{id}'
        return self.http_repo.update_data_api(base_url=url, body=data)

    def delete_json_placeholder(self, id: str) -> dict:
        url = f'{self.url}/posts/{id}'
        return self.http_repo.delete_data_api(base_url=url)
