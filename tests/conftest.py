import os

import pytest
from dotenv import load_dotenv
from selene import browser
from selene.support.shared import config
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selene import Browser, Config
from configure.utils import attach

def pytest_addoption(parser):
    parser.addoption(
        '--browser',
        help='Браузер, в котором запущены тесты',
        choices=['firefox', 'chrome'],
        default='chrome'
    )

@pytest.fixture(scope='session')
def browser_name(request):
    return request.config.getoption('--browser')

@pytest.fixture(scope='session', autouse=True)
def load_env():
    load_dotenv()

@pytest.fixture(scope='function', autouse=True)
def browser_manager(browser_name):
    options = Options()
    selenoid_capabilities = {
        "browserName": browser_name,
        "browserVersion": "100.0",
        "selenoid:options": {"enableVNC": True, "enableVideo": True}
    }

    options.capabilities.update(selenoid_capabilities)

    login = os.getenv('LOGIN')
    password = os.getenv('PASSWORD')

    driver = webdriver.Remote(
        command_executor=f"https://{login}:{password}@selenoid.autotests.cloud/wd/hub",
        options=options)

    # browser = Browser(Config(driver))

    browser.config.driver = driver

    browser.config.base_url = 'https://demoqa.com/automation-practice-form'
    browser.config.timeout = 4.0
    browser.config.type_by_js = True


    yield browser

    attach.add_screenshot(browser)
    attach.add_logs(browser)
    attach.add_html(browser)
    attach.add_video(browser)
    browser.quit()