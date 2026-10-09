from appium.webdriver.common.appiumby import AppiumBy
from pages.base.base_page import BasePage
import time

class LoginPage(BasePage):

    DAVOM_ETISH = (AppiumBy.ACCESSIBILITY_ID, "Давом этиш")
    PHONE_CONTAINER = (AppiumBy.ACCESSIBILITY_ID, "+7 ") 
    PHONE_INPUT = (AppiumBy.CLASS_NAME, "android.widget.EditText")

    def tap_davom_etish(self):
        self.click(self.DAVOM_ETISH)

    def onboarding(self):
        # 4 slaydni o'tkazsh
        for _ in range(4):
               self.tap_davom_etish()
               time.sleep(1)

    def enter_phone(self, phone):
        # self.send_keys(self.PHONE_INPUT, phone)  # boshda bosish uchun
        # time.sleep(2)
        # self.send_keys(self.PHONE_INPUT, phone)
        # self.tap_davom_etish()
        # inputni bosish
        self.click(self.PHONE_INPUT)
        time.sleep(2)

        # klaviaturada yozamiz
        self.driver.execute_script("mobile: type", {"text": phone})
        time.sleep(1)
        self.tap_davom_etish()

    def login(self, phone):
         self.onboarding()
         time.sleep(3)
         self.enter_phone(phone)

time.sleep(3)