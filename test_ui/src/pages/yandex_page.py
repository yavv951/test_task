import time

import allure

from test_ui.src.locators.yandex_locators import YandexPageLocators
from test_ui.src.models.constants import Constants
from test_ui.src.pages.base_page import BasePage


class YandexPage(BasePage):
    """
     Методы страницы Яндекс
    """

    @allure.step("Кликаем на кнопку Войти на главной странице")
    def click_button_enter_main_page(self):
        self.click_element_by(index=0, locator=YandexPageLocators.BUTTON_ENTER_MAIN)
        return self

    @allure.step("Заполняем поле логин")
    def fill_field_login(self):
        self.fill_element(locator=YandexPageLocators.LOGIN, text='yvv951')
        return self

    @allure.step("Заполняем поле пароль")
    def fill_field_password(self):
        self.fill_element(locator=YandexPageLocators.PASSWORD, text='T#sttest1234')
        return self

    @allure.step("Кликаем на кнопку Войти")
    def click_button_enter(self):
        self.click_element(YandexPageLocators.BUTTON_ENTER)
        return self

    @allure.step("Проверяем,что пользователь авторизовался")
    def check_auth_in_mail(self):
        self.check_element_have_text_(locator=YandexPageLocators.AUTH_NAME, text='yvv951')
        return self

    @allure.step("Кликаем на кнопу 'Почта', для перехода в почтовый ящик")
    def click_button_mail(self):
        self.click_element(YandexPageLocators.BUTTON_MAIL)
        return self

    @allure.step("Проверяем,что пользователь перешел в почтовый ящик")
    def check_user_went_mail(self):
        self.check_element_have_text_(locator=YandexPageLocators.TEXT_IN_MAIL, text=Constants.TEXT_YANDEX)
        time.sleep(2)
        return self

    @allure.step("Переключаемся на второе окно")
    def switch_to_new_window(self):
        self.switch_to_window(index=1)
        return self
