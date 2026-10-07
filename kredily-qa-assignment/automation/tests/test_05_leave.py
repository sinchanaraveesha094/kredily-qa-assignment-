from pages.dashboard_page import DashboardPage
from pages.leave_page import LeavePage


def test_leave_balance_and_apply_form(logged_in):
    """TC18 (read-only) - leave balance is shown and the apply form opens."""
    DashboardPage(logged_in).open_leave()
    page = LeavePage(logged_in)
    assert page.balance_visible(), "Leave balance not displayed"
    page.open_apply_form()
    assert page.form_visible(), "Apply-leave form did not open / expected fields missing"
