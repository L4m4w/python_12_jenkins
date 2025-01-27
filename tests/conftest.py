import pytest
from selene import browser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selene import Browser, Config
from configure.utils import attach


@pytest.fixture(scope='function', autouse=True)
def browser_manager():
    options = Options()
    selenoid_capabilities = {
        "browserName": "chrome",
        "browserVersion": "100.0",
        "selenoid:options": {"enableVNC": True, "enableVideo": True}
    }

    options.capabilities.update(selenoid_capabilities)

    driver = webdriver.Remote(
        command_executor=f"https://user1:1234@selenoid.autotests.cloud/wd/hub",
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