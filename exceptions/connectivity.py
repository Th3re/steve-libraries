import requests


class APIError(Exception):
    def __init__(self, response: requests.Response):
        self.response = response

    def __repr(self):
        return f'<{self.__class__.__name__}>[status_code: \"{self.response.status_code}\", content: \"{self.response.content}\"]'

    def __repr__(self):
        return self.__repr()

    def __str__(self):
        return self.__repr()


class AuthenticationError(APIError):
    pass


class UnknownConnectivityError(APIError):
    pass
