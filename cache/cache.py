import abc

from typing import Optional, Any


class Cache(abc.ABC):
    @abc.abstractmethod
    def set(self, key, value, ttl):
        pass

    @abc.abstractmethod
    def get(self, key) -> Optional[Any]:
        pass
