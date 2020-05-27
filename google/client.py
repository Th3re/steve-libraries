import abc


class Client(abc.ABC):
    @abc.abstractmethod
    def get(self, endpoint, token, params):
        pass

    @abc.abstractmethod
    def post(self, endpoint, token, params, body):
        pass
