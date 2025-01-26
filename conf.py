import pytest
from selene import browser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from utils import attach


@pytest.fixture(scope='function', autouse=True)
def browser_manager():
    browser.config.base_url = 'https://demoqa.com/automation-practice-form'
    browser.config.timeout = 4.0
    browser.config.type_by_js = True

    driver_options = webdriver.ChromeOptions()
    #driver_options.add_argument('--headless')

    browser.config.driver_options = driver_options
    options = Options()
    selenoid_capabilities = {
        "browserName": "chrome",
        "browserVersion": "123.0",
        "selenoid:options": {
            "enableVideo": False
        }
    }

    options.capabilities.update(selenoid_capabilities)

    driver = webdriver.Remote(
        command_executor="https://selenoid.autotests.cloud/wd/hub",
        options=options)

    browser.config.driver = driver

    yield browser

    attach.add_screenshot(browser)
    attach.add_logs(browser)
    attach.add_html(browser)
    attach.add_video(browser)

    browser.quit()