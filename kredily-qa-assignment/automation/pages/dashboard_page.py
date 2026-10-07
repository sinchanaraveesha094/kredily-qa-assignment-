from pages.base_page import BasePage, either


class DashboardPage(BasePage):
    # VERIFY labels against the real navigation entries.
    ATTENDANCE = either(r".*attendance.*")
    LEAVE = either(r".*leave.*")

    def has_core_sections(self) -> dict:
        return {
            "attendance": self.exists(*self.ATTENDANCE, timeout=10),
            "leave": self.exists(*self.LEAVE, timeout=10),
        }

    def open_attendance(self):
        self.tap(*self.ATTENDANCE)

    def open_leave(self):
        self.tap(*self.LEAVE)
