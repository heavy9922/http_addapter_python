from injector import Module, Binder

from app.repositories.base_http import BaseRepositoryHttp
from infrastrcture.repository_impl_http import HttpRepository


class AppModuleHttp(Module):
    def configure(self, binder: Binder):
        binder.bind(BaseRepositoryHttp, to=HttpRepository)
