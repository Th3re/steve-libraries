import abc
from typing import Optional, Any


class Store(abc.ABC):
    @abc.abstractmethod
    def save(self, identifier, data):
        pass

    @abc.abstractmethod
    def get(self, identifier) -> Optional[Any]:
        pass
