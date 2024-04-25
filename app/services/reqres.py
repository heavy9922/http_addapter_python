from app.repositories.base_http import BaseRepositoryHttp


class ReqresServices:
    def __init__(self, http_repo: BaseRepositoryHttp):
        self.http_repo = http_repo
        self.url = 'https://reqres.in/api'

    def create_reqres(self, data: dict) -> dict:
        url = f'{self.url}/users'
        return self.http_repo.create_data_api(base_url=url, body=data)

    def get_reqres(self):
        url = f'{self.url}/users'
        return self.http_repo.get_data_api(base_url=url, response_type='json')

    def update_reqres(self, id: str, data: dict) -> dict:
        url = f'{self.url}/users/{id}'
        return self.http_repo.update_data_api(base_url=url, body=data)

    def delete_reqres(self, id: str) -> dict:
        url = f'{self.url}/users/{id}'
        return self.http_repo.delete_data_api(base_url=url)
