import os
import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options

import config


@pytest.fixture(scope="function")
def driver():
    opts = UiAutomator2Options()
    opts.platform_name = "Android"
    opts.automation_name = "UiAutomator2"
    opts.device_name = config.DEVICE_NAME
    opts.app = config.APK_PATH          # installs & launches; no package/activity needed
    opts.auto_grant_permissions = True
    opts.no_reset = False               # clean state for every test
    opts.new_command_timeout = 300
    drv = webdriver.Remote(config.APPIUM_URL, options=opts)
    drv.implicitly_wait(0)              # explicit waits only
    yield drv
    drv.quit()


@pytest.fixture
def logged_in(driver):
    from pages.login_page import LoginPage
    page = LoginPage(driver)
    page.login(config.EMAIL, config.PASSWORD)
    assert page.is_logged_in(), "Precondition failed: could not log in"
    return driver


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    if rep.when == "call" and rep.failed:
        drv = item.funcargs.get("driver")
        if drv:
            os.makedirs(config.SCREENSHOT_DIR, exist_ok=True)
            drv.save_screenshot(os.path.join(config.SCREENSHOT_DIR, f"FAIL_{item.name}.png"))
