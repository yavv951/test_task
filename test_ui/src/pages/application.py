from test_ui.src.pages.base_page import BasePage
from test_ui.src.pages.google_page import GooglePage
from test_ui.src.pages.yandex_page import YandexPage


class Application:
    def __init__(self, base_url):
        self.url = base_url
        self.google_page = GooglePage(self)
        self.yandex_page =YandexPage(self)

    @staticmethod
    def close():
        BasePage.close()

