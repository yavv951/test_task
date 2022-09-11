import allure
import pytest
from allure_commons.types import Severity

from test_api.endpoints_models.register.model import ResponseReqres

@pytest.mark.api_test
@allure.tag('WEB API')
@allure.severity(Severity.CRITICAL)
@allure.label('Owner', 'Vadim')
@allure.feature('Testing site reqres with selene')
@allure.story(f'Тест кейс 0001 Найти пользователя по UUID')
@allure.link('https://github.com/yavv951', name='Owner')
def test_get_user(app) -> None:
    """Тест кейс: Найти пользователя по UUID"""
    response = app.reqres.get(user_id=2, type_response=ResponseReqres)
    assert response.status_code == 200, "Check code"
    assert response.data.data.first_name == "Janet"


@pytest.mark.api_test
@allure.tag('WEB API')
@allure.severity(Severity.CRITICAL)
@allure.label('Owner', 'Vadim')
@allure.feature('Testing site reqres with selene')
@allure.story(f'Тест кейс 0002 Получить всех пользователей')
@allure.link('https://github.com/yavv951', name='Owner')
def test_all_users(app) -> None:
    """Тест кейс: Получить всех пользователей"""
    response = app.reqres.get(user_id=None, type_response=None)
    assert response.status_code == 200, "Check code"



