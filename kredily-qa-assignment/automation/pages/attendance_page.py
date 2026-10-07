from pages.base_page import BasePage, either


class AttendancePage(BasePage):
    # VERIFY wording: Check In / Punch In / Clock In ...
    ACTION_BTN = either(r".*(check ?-? ?(in|out)|punch ?-? ?(in|out)|clock ?-? ?(in|out)).*")
    HISTORY = either(r".*(history|log|calendar|today|present|absent|hours).*")

    def action_button_visible(self) -> bool:
        return self.exists(*self.ACTION_BTN, timeout=15)

    def history_visible(self) -> bool:
        return self.exists(*self.HISTORY, timeout=10)

    def tap_action(self):
        self.tap(*self.ACTION_BTN)
