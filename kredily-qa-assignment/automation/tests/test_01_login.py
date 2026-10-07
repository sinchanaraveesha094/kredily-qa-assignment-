import config
from pages.login_page import LoginPage


def test_valid_login(driver):
    """TC01 - valid credentials land on the dashboard."""
    page = LoginPage(driver)
    page.login(config.EMAIL, config.PASSWORD)
    assert page.is_logged_in(), "Dashboard not reached after valid login"
