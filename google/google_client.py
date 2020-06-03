import logging

import requests

from .client import Client
from ..exceptions.connectivity import AuthenticationError, UnknownConnectivityError

LOG = logging.getLogger(__name__)
requests_log = logging.getLogger("requests.packages.urllib3")
requests_log.setLevel(logging.DEBUG)
requests_log.propagate = True


class GoogleClient(Client):
    def __init__(self, host):
        self.host = host

    def _request(self, endpoint, token, method, params=None, body=None):
        url = f'{self.host}/{endpoint}'
        headers = {}
        if token:
            headers['Authorization'] = f'Bearer {token}'
        response = method(url, params=params, headers=headers, json=body)
        LOG.debug(response)
        if 200 <= response.status_code < 300:
            return response.json()
        if response.status_code == 401:
            raise AuthenticationError(response)
        else:
            raise UnknownConnectivityError(response)

    def get(self, endpoint, token, params):
        return self._request(endpoint, token, requests.get, params)

    def post(self, endpoint, token, params, body):
        return self._request(endpoint, token, requests.post, params, body)
