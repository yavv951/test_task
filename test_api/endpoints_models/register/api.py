import allure
from pydantic import BaseModel

from test_api.utils.logger import logging_deco as log
from test_api.utils.validator import Validator


class Reqres(Validator):
    """API endpoint get /users/{id}."""

    GET_USER = "/users/"

    def __init__(self, app):
        self.app = app

    @allure.step("GET Запрос Получаем пользователя по UUID или список пользователей")
    @log("GET USERS")
    def get(self, user_id: int, type_response: BaseModel):
        """Get request."""
        if user_id:
            response = self.app.client.request(
                method="GET",
                url=f"{self.app.url}{self.GET_USER}{user_id}"
            )
        else:
            response = self.app.client.request(
                method="GET",
                url=f"{self.app.url}{self.GET_USER}"
            )
        return self.structure(response, type_response=type_response)
