from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait

from pages.base_page import BasePage, either


class LoginPage(BasePage):
    # VERIFY with Appium Inspector – prefer resource-id / accessibility id once known.
    EDIT_TEXTS = (AppiumBy.CLASS_NAME, "android.widget.EditText")
    LOGIN_BTN = either(r".*(log ?in|sign ?in).*")
    ERROR_MSG = either(r".*(invalid|incorrect|wrong|failed|not found|unable|error).*")
    HOME_MARKERS = either(r".*(attendance|leave|dashboard|home|welcome).*")  # VERIFY

    def _fields(self):
        self.wait_for(self.EDIT_TEXTS)
        fields = self.driver.find_elements(*self.EDIT_TEXTS)
        assert len(fields) >= 2, f"Expected email+password fields, found {len(fields)}"
        return fields[0], fields[1]   # VERIFY order: email first, password second

    def login(self, email, password):
        email_el, pass_el = self._fields()
        self.type_into(email_el, email)
        self.type_into(pass_el, password)
        self.hide_keyboard()
        self.tap(*self.LOGIN_BTN)

    def _home_and_no_login_fields(self, d):
        home = any(d.find_elements(*loc) for loc in self.HOME_MARKERS)
        return home and not d.find_elements(*self.EDIT_TEXTS)

    def is_logged_in(self, timeout=30) -> bool:
        try:
            WebDriverWait(self.driver, timeout).until(self._home_and_no_login_fields)
            return True
        except TimeoutException:
            return False

    def on_login_screen(self) -> bool:
        return len(self.driver.find_elements(*self.EDIT_TEXTS)) >= 2

    def error_shown(self, timeout=10) -> bool:
        return self.exists(*self.ERROR_MSG, timeout=timeout)
