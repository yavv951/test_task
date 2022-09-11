import pytest

from test_api.endpoints_models.app import ReqresApp


@pytest.fixture()
def app(request) -> ReqresApp:
    url = request.config.getoption("--api-url")
    return ReqresApp(url)


def pytest_addoption(parser):
    parser.addoption(
        "--api-url",
        action="store",
        help="enter api url",
        default="https://reqres.in/api",
    )
