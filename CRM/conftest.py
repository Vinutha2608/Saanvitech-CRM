import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

from CRM.pages.login_page import LoginPage
from CRM.utils.config_reader import get_config
from CRM.utils.excel_reader import get_excel_data


def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        help="Browser: chrome, edge, firefox"
    )


@pytest.fixture(scope='session')
def setup(request):
    browser = request.config.getoption("--browser")
    if browser == "chrome":
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    elif browser == "edge":
        driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
    elif browser == "firefox":
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    else:
        raise Exception("browser not supported")
    driver.get(get_config("url"))
    driver.maximize_window()
    yield driver
    driver.close()

@pytest.fixture(scope='function')
def login(setup):
    driver = setup
    lp = LoginPage(driver)

    # take first row from excel
    data = get_excel_data("login")[0]
    business_email = data[0]
    password = data[1]

    lp.verify_login(business_email, password)
    # assert "SaanviTech Dashboard" in driver.page_source
    return driver




