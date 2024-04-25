from abc import ABC, abstractmethod
from typing import TypeVar, List, Optional

DataType = TypeVar('DataType')
ModelType = TypeVar('ModelType')


class BaseRepositoryHttp(ABC):
    @abstractmethod
    def get_data_api(self, base_url: str, headers=None, response_type=None) -> List[DataType]:
        pass

    @abstractmethod
    def create_data_api(self, base_url: str, body=None, headers=None) -> DataType:
        pass

    @abstractmethod
    def update_data_api(self, base_url: str, body=None, headers=None) -> ModelType:
        pass

    @abstractmethod
    def delete_data_api(self, base_url: str, headers=None):
        pass
