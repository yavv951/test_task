from test_api.endpoints_models.register.api import Reqres
from test_api.utils.client import Client


class ReqresApp:
    """App."""

    def __init__(self, url: str):
        self.url = url
        self.client = Client
        self.reqres = Reqres(self)
