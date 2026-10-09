from appium.webdriver.common.appiumby import AppiumBy
from pages.base.base_page import BasePage
import time


class TelefonPage(BasePage):

    TELEFON_INPUT = (AppiumBy.CLASS_NAME, "android.widget.EditText")
    BANK_TANLANG = (AppiumBy.ACCESSIBILITY_ID, "Банкни танланг")
    DAVOM_ETISH = (AppiumBy.XPATH, '//android.widget.Button[@content-desc="Давом этиш"]')
    HAMKORBANK = (AppiumBy.ACCESSIBILITY_ID, "Hamkorbank")

    def enter_phone(self, phone: str):
        input_field = self.driver.find_element(*self.TELEFON_INPUT)
        input_field.click()
        time.sleep(1)
        input_field.send_keys(phone)
        time.sleep(1)
        self.driver.hide_keyboard()
        time.sleep(1)

    def tap_bank_tanlang(self):
        self.click(self.BANK_TANLANG)

    def tap_davom_etish(self):
        self.click(self.DAVOM_ETISH)

    def select_hamkorbank(self):
        self.driver.execute_script("mobile: scrollGesture", {
            "left": 31, "top": 516, "width": 568, "height": 800, 
            "direction": "down",
            "percent": 0.5
        })
        time.sleep(1)
        self.click(self.HAMKORBANK)