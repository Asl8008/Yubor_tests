from appium.webdriver.common.appiumby import AppiumBy
from pages.base.base_page import BasePage


class HelpPage(BasePage):

    SARLAVHA = (AppiumBy.ACCESSIBILITY_ID, "Қўллаб-қувватлаш")
    ONLAYN_CHAT = (AppiumBy.ACCESSIBILITY_ID, "Онлайн чат")
    TELEGRAM = (AppiumBy.ACCESSIBILITY_ID, "Telegram")
    ELEKTRON_POCHTA = (AppiumBy.ACCESSIBILITY_ID, "Электрон почта")

    def is_yordam_page(self) -> bool:
        try:
            self.wait.until(lambda d: d.find_element(*self.SARLAVHA))
            return True
        except Exception:
            return False

    def tap_onlayn_chat(self):
        self.click(self.ONLAYN_CHAT)

    def tap_telegram(self):
        self.click(self.TELEGRAM)

    def tap_elektron_pochta(self):
        self.click(self.ELEKTRON_POCHTA)
