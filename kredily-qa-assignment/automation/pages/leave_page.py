from pages.base_page import BasePage, either


class LeavePage(BasePage):
    # VERIFY labels.
    APPLY_BTN = either(r".*(apply|request|new).*")
    BALANCE = either(r".*(balance|available|remaining|casual|sick|earned).*")
    FORM_MARKERS = either(r".*(leave type|from|to|reason|start|end).*")

    def balance_visible(self) -> bool:
        return self.exists(*self.BALANCE, timeout=15)

    def open_apply_form(self):
        self.tap(*self.APPLY_BTN)

    def form_visible(self) -> bool:
        return self.exists(*self.FORM_MARKERS, timeout=10)
