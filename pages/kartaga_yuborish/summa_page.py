from appium.webdriver.common.appiumby import AppiumBy
from pages.base.base_page import BasePage
import time


class SummaPage(BasePage):

    SUMMA_INPUT = (AppiumBy.CLASS_NAME, "android.widget.EditText")
    DAVOM_ETISH = (AppiumBy.ACCESSIBILITY_ID, "Давом этиш")
    OK_BUTTON = (AppiumBy.ACCESSIBILITY_ID, "Ок")
    VALYUTA = (AppiumBy.XPATH, '//android.widget.ImageView[@content-desc="Валюта\nUZS"]')
    RUB = (AppiumBy.ACCESSIBILITY_ID, "RUB")

    def enter_summa(self, summa: str):
        input_field = self.driver.find_element(*self.SUMMA_INPUT)
        input_field.click()
        time.sleep(1)
        input_field.clear()
        input_field.send_keys(summa)
        time.sleep(1)
        self.driver.hide_keyboard()
        time.sleep(1)

    def tap_davom_etish(self):
        self.click(self.DAVOM_ETISH)

    def tap_ok(self):
        self.click(self.OK_BUTTON)

    def tap_valyuta(self):
        self.click(self.VALYUTA)

    def select_rub(self):
        self.click(self.RUB)