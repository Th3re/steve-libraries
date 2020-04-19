import os

from ..representation.environment import EnvPrint


class EnvironmentReader(EnvPrint):
    def get(self, name: str) -> str:
        env_name = f'{self.__class__.__name__.upper()}_{name.upper()}'
        return os.environ[env_name]
