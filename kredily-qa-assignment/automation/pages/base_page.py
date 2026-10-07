from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

import config


def ui(selector: str):
    return (AppiumBy.ANDROID_UIAUTOMATOR, selector)


def text_matches(regex: str):
    """Case-insensitive regex on visible text."""
    return ui(f'new UiSelector().textMatches("(?i){regex}")')


def desc_matches(regex: str):
    """Case-insensitive regex on content-desc (used by Flutter/RN apps)."""
    return ui(f'new UiSelector().descriptionMatches("(?i){regex}")')


def either(regex: str):
    return [text_matches(regex), desc_matches(regex)]


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def wait_for(self, locator, timeout=config.DEFAULT_TIMEOUT):
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))

    def exists(self, *locators, timeout=5) -> bool:
        def _any(d):
            return any(d.find_elements(*loc) for loc in locators)
        try:
            WebDriverWait(self.driver, timeout).until(_any)
            return True
        except TimeoutException:
            return False

    def tap(self, *locators, timeout=config.DEFAULT_TIMEOUT):
        def _first(d):
            for loc in locators:
                els = d.find_elements(*loc)
                if els:
                    return els[0]
            return False
        WebDriverWait(self.driver, timeout).until(_first).click()

    def type_into(self, element, value):
        element.click()
        element.clear()
        element.send_keys(value)

    def hide_keyboard(self):
        try:
            self.driver.hide_keyboard()
        except Exception:
            pass
