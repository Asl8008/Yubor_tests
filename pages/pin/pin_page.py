from appium.webdriver.common.appiumby import AppiumBy
from pages.base.base_page import BasePage


class PinPage(BasePage):

    # Raqam tugmalari - content-desc orqali
    def get_digit(self, digit: str):
        return (AppiumBy.ACCESSIBILITY_ID, digit)
    
    def enter_pin(self, pin: str):
        """PIN kiritish - har bir raqamni bosadi"""
        for digit in pin:
            self.click(self.get_digit(digit))
    
    def enter_full_pin_flow(self, pin: str):
        """PIN kiritish + tasdiqlash"""
        # 1. PIN kiritish
        self.enter_pin(pin)
        import time
        time.sleep(2)
        # 2. Tasdiqlash ekranida ham xuddi shunday
        self.enter_pin(pin)
