import allure
import pytest
from allure_commons.types import Severity

@pytest.mark.ui_test
@allure.tag('WEB UI')
@allure.severity(Severity.CRITICAL)
@allure.label('Owner', 'Vadim')
@allure.feature('Testing site google with selene')
@allure.story(f'Тест кейс 0001 Проверка поля поиска Гугл')
@allure.link('https://github.com/yavv951', name='Owner')
def test_search_google(app_go):
    """Автотест на гугл-поиск"""
    app_go.google_page.input_value_on_field_and_press_enter()
    fields = app_go.google_page.calculate_field()
    assert fields >= 10
    app_go.google_page.check_have_cite_mvideo_on_page()



