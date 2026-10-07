import pytest
import config
from pages.login_page import LoginPage


@pytest.mark.parametrize("email,password", [
    (config.EMAIL, "WrongPass@123"),                  # TC02 wrong password
    ("nobody.registered@yopmail.com", "Pass@9865"),   # TC03 unknown user
])
def test_invalid_login_is_rejected(driver, email, password):
    page = LoginPage(driver)
    page.login(email, password)
    assert not page.is_logged_in(timeout=8), "Invalid credentials must not log in"
    assert page.error_shown() or page.on_login_screen(), "Neither error nor login screen visible"
