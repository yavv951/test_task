from selene import *
from selene.support.shared import browser
from selene.support.conditions import have, be


class BasePage:
    def __init__(self, app):
        self.app = app

    @staticmethod
    def fill_element(locator, text):
        browser.element(locator).type(text)

    @staticmethod
    def fill_element_and_press_enter(locator, text):
        browser.element(locator).type(text).press_enter()

    @staticmethod
    def click_element(locator):
        browser.element(locator).should(be.clickable).click()

    @staticmethod
    def click_element_by(locator, index):
        browser.all(locator)[index].click()


    @staticmethod
    def check_element_have_text(locator, text):
        browser.element(locator).should(have.text(text))

    @staticmethod
    def cells_of_row(index, locator, locator_2, locator_3, text, text_2):
        """ метод по работе с табличными данными, применим когда необходимо по строкам определить введенный текст"""
        browser.element(locator).all(locator_2)[index].all(locator_3).should(have.exact_texts(text, text_2))

    @staticmethod
    def check_element_have_text_by(index, locator, text):
        browser.all(locator)[index].should(have.text(text))

    @staticmethod
    def check_element_have_text_(locator, text):
        browser.all(locator).should(have.text(text))


    @staticmethod
    def check_element_have_attr(locator, attr_name, value):
        browser.element(locator).should(have.attribute(attr_name, value))

    @staticmethod
    def get_element_text(locator):
        return browser.element(locator).text

    @staticmethod
    def element_have_value(locator, text):
        browser.element(locator).should(have.attribute("value", text))

    @staticmethod
    def get_element_attr(locator):
        return browser.element(locator).get_attribute()

    @staticmethod
    def size_line(locator):
        return browser.all(locator)

    @staticmethod
    def find_element(locator, locator_2):
        return browser.all('option').element(locator).element(locator_2).click()

    @staticmethod
    def close():
        return browser.close_current_tab()

    @staticmethod
    def scroll_metod(x=0, y=0):
        """ Метод скрола на странице, в х и у указыватюся координаты страницы"""
        # browser.perform(Scroll.scroll_by_offset(x, y))
        browser.execute_script(f'window.scrollTo{x, y}')

    @staticmethod
    def switch_to_window(index: int):
        """ Метод переключения между окнами страницы,в скобках указывается индекс страницы,отсчет идет с 0"""
        browser.switch_to_tab(index)

    @staticmethod
    def hover_element(locator):
        """ Метод наведения курсора на поле"""
        browser.element(locator).hover()

    @staticmethod
    def select(locator, locator_2, option):
        """Функция для работы с select элементами"""
        browser.element(locator).perform(command.js.scroll_into_view).click()
        browser.all(locator_2).element_by(have.exact_text(option)).click()


