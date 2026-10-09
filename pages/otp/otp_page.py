from appium.webdriver.common.appiumby import AppiumBy
from pages.base.base_page import BasePage


class OtpPage(BasePage):

    # Locatorlar
    OTP_INPUT = (AppiumBy.XPATH, "//android.widget.EditText")
    DAVOM_ETISH = (AppiumBy.ACCESSIBILITY_ID, "Давом этиш")

    def enter_otp(self, otp):
        self.send_keys(self.OTP_INPUT, otp)
    #     self.tap_davom_etish()

    # def tap_davom_etish(self):
    #     self.click(self.DAVOM_ETISH)