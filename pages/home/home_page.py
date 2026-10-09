from appium.webdriver.common.appiumby import AppiumBy
from pages.base.base_page import BasePage


class HomePage(BasePage):

    # Bottom navigation
    ASOSIY = (AppiumBy.ACCESSIBILITY_ID, "Асосий\nВкладка 1 из 5")
    TARIX = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().descriptionContains("Тарих")')
    OTKAZISH = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().descriptionContains("Ўтказиш")')
    YORDAM = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().descriptionContains("Ёрдам")')
    PROFIL = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().descriptionContains("Профил")')

    # Asosiy tugmalar
    KARTAGA_YUBORISH = (AppiumBy.ACCESSIBILITY_ID, "Картага юбориш")
    NAQD_PUL_YUBORISH = (AppiumBy.ACCESSIBILITY_ID, "Нақд пул юбориш")
    BARCHASI = (AppiumBy.ACCESSIBILITY_ID, "Барчаси")
    VALYUTA_KURSLARI = (AppiumBy.ACCESSIBILITY_ID, "Валюта курслари")

    def is_home_page(self) -> bool:
        """Home page ochilganligini tekshiradi."""
        try:
            self.wait.until(
                lambda d: d.find_element(AppiumBy.ACCESSIBILITY_ID, "Картага юбориш")
            )
            return True
        except Exception:
            return False

    def scroll_bottom(self):
        """Sahifani oxirigacha scroll qiladi."""
        self.driver.find_element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiScrollable(new UiSelector().scrollable(true)).scrollToEnd(10)',
        )


    # Tab navigatsiya
    def go_to_tarix(self):
        self.click(self.TARIX)

    def go_to_otkazish(self):
        self.click(self.OTKAZISH)

    def go_to_yordam(self):
        self.click(self.YORDAM)

    def go_to_profil(self):
        self.click(self.PROFIL)

    # Asosiy funksiyalar
    def tap_kartaga_yuborish(self):
        self.click(self.KARTAGA_YUBORISH)

    def tap_naqd_pul_yuborish(self):
        self.click(self.NAQD_PUL_YUBORISH)

    def tap_barchasi(self):
        self.click(self.BARCHASI)
