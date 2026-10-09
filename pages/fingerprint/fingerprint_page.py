from appium.webdriver.common.appiumby import AppiumBy
from pages.base.base_page import BasePage


class FingerprintPage(BasePage):
    
    SKIP_BUTTON = (AppiumBy.ACCESSIBILITY_ID, "Ўтказиб юбориш")
    
    def skip(self):
        self.click(self.SKIP_BUTTON)