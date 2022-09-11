import allure

from test_ui.src.locators.google_locators import GooglePageLocators
from test_ui.src.models.constants import Constants
from test_ui.src.pages.base_page import BasePage


class GooglePage(BasePage):
    """
    Страница Practice Form
    """

    @allure.step(f"Вводим значение в поле поиска {Constants.TEXT}")
    def input_value_on_field_and_press_enter(self):
        """Ввод данных в поле поиска"""
        self.fill_element_and_press_enter(locator=GooglePageLocators.FIELD_SEARCH, text=Constants.TEXT)
        return self

    @allure.step("Подсчитываем количество ответов")
    def calculate_field(self):
        element = self.size_line(GooglePageLocators.FIELDS)
        return len(element)


    @allure.step("Кликаем на кнопку 'Закрыть'")
    def check_have_cite_mvideo_on_page(self):
        self.check_element_have_text_(locator=GooglePageLocators.FIELD_CITES, text=Constants.MVIDEO_LINK)
        return self
