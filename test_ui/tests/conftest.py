import pytest
from selene.support.shared import browser

from dotenv import load_dotenv

from test_ui.src.pages.application import Application


def pytest_addoption(parser):
    parser.addoption(
        '--browser_version',
        default='100.0'
    )
    parser.addoption(
        "--google-url",
        action="store",
        default="https://www.google.com/",
        help="enter base_url"
    )

    parser.addoption(
        "--yandex-url",
        action="store",
        default="https://yandex.ru",
        help="enter base_url"
    )


@pytest.fixture(scope='session', autouse=True)
def load_env():
    load_dotenv()


@pytest.fixture
def app_go(request):
    base_url = request.config.getoption("--google-url")
    browser.open(base_url).driver.set_window_size(width=1980, height=1280)
    app = Application(base_url)
    yield app
    app.close()


@pytest.fixture
def app_ya(request):
    base_url = request.config.getoption("--yandex-url")
    browser.open(base_url).driver.set_window_size(width=1980, height=1280)
    app = Application(base_url)
    yield app
    app.close()
