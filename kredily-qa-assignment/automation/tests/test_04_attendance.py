from pages.dashboard_page import DashboardPage
from pages.attendance_page import AttendancePage


def test_attendance_screen(logged_in):
    """TC15 (read-only) - attendance opens and exposes a check-in/out control.
    Check-in is intentionally not tapped so the shared account stays clean;
    add page.tap_action() plus a success assertion to execute a real punch."""
    DashboardPage(logged_in).open_attendance()
    page = AttendancePage(logged_in)
    assert page.action_button_visible(), "No check-in/check-out control found"
