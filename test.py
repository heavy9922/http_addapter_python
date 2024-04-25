import json

from injector import Injector
from app import AppModuleHttp
from app.repositories.base_http import BaseRepositoryHttp
from app.services.jsonplaceholder import JsonPlaceholderServices
from app.services.reqres import ReqresServices

injector_http = Injector([AppModuleHttp()])
http_repo = injector_http.get(BaseRepositoryHttp)
json_services = JsonPlaceholderServices(http_repo)
reqres_services = ReqresServices(http_repo)


def main():
    data = {
        'title': "New Title",
        'body': "New body content",
        'userId': 1
    }
    print(json_services.create_json_placeholder(data))
    print(json_services.get_json_placeholder(), 'XD')
    print(json_services.get_json_placeholder_by_id(1), 'XD2')
    print(json_services.update_json_placeholder(1, data), 'XD3')
    print(json_services.delete_json_placeholder(1), 'XD4')
    data = {
        'name': 'pepito',
        'job': 'developer'
    }
    print(reqres_services.create_reqres(data))
    print(json.dumps(reqres_services.get_reqres()), 'XD')
    print(reqres_services.update_reqres(1, data), 'XD2')
    print(reqres_services.delete_reqres(1), 'XD3')


if __name__ == '__main__':
    main()
