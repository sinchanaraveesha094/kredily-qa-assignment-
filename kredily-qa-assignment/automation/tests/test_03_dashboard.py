from pages.dashboard_page import DashboardPage


def test_dashboard_core_sections(logged_in):
    """TC13 - dashboard renders the main HRMS sections."""
    sections = DashboardPage(logged_in).has_core_sections()
    missing = [k for k, v in sections.items() if not v]
    assert not missing, f"Dashboard missing sections: {missing}"
