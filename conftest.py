from data.data_static import get_static_data
from data.models import (
    Account,
    CCMessage,
)
from data import (
    generate_unique_username,
)
import pytest
from pytest import fixture
from selenium import (
    webdriver,
)
from pages import (
    AccountOverviewPage,
    ContactUsPage,
    HomePage,
    RegisterPage,
    RegistrationSuccessPage,
)
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.utils import ChromeType


@fixture(scope="session")
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    d = webdriver.Chrome(ChromeDriverManager(chrome_type=ChromeType.GOOGLE).install(), options=options)
    d.maximize_window()
    yield d

    d.close()


@fixture(scope="session")
def normal_user(env):
    yield Account(**get_static_data('test', 'normal_user'))


@fixture(scope="function")
def new_user():
    account = Account()
    account.username = generate_unique_username()
    account.password = 'Password'
    yield account


@fixture(scope="function")
def cc_message():
    yield CCMessage()


@fixture(scope="session")
def account_overview_page(driver):
    yield AccountOverviewPage(driver)


@fixture(scope="session")
def contact_us_page(driver):
    yield ContactUsPage(driver)


@fixture(scope="session")
def home_page(driver):
    yield HomePage(driver)


@fixture(scope="session")
def register_page(driver):
    yield RegisterPage(driver)


@fixture(scope="session")
def registration_success_page(driver):
    yield RegistrationSuccessPage(driver)


def pytest_addoption(parser):
    parser.addoption("--env", action="store", default="TEST")


def pytest_runtest_makereport(item, call):
    if "incremental" in item.keywords:
        if call.excinfo is not None:
            parent = item.parent
            parent._previousfailed = item


def pytest_runtest_setup(item):
    if "incremental" in item.keywords:
        previousfailed = getattr(item.parent, "_previousfailed", None)
        if previousfailed is not None:
            pytest.xfail("previous test failed ({})".format(previousfailed.name))


def pytest_generate_tests(metafunc):
    option_value = metafunc.config.option.env
    if 'env' in metafunc.fixturenames and option_value is not None:
        metafunc.parametrize("env", [option_value], scope='session')
