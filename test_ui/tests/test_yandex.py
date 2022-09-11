import allure
import pytest
from allure_commons.types import Severity

@pytest.mark.ui_test
@allure.tag('WEB UI')
@allure.severity(Severity.CRITICAL)
@allure.label('Owner', 'Vadim')
@allure.feature('Testing site yandex with selene')
@allure.story(f'Тест кейс 0002 Вход в почтовый ящик Яндекса')
@allure.link('https://github.com/yavv951', name='Owner')
def test_web_tables(app_ya):
    """Вход в почтовый ящик Яндекса"""
    app_ya.yandex_page. \
        click_button_enter_main_page() \
        .fill_field_login() \
        .click_button_enter() \
        .fill_field_password() \
        .click_button_enter() \
        .check_auth_in_mail() \
        .click_button_mail() \
        .switch_to_new_window() \
        .check_user_went_mail()
