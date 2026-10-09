from appium.webdriver.common.appiumby import AppiumBy
from pages.base.base_page import BasePage


class NaqdPage(BasePage):

    # Sahifa sarlavhasi
    SARLAVHA = (AppiumBy.ACCESSIBILITY_ID, "АҚШ доллари юбориш")

    # Info blok (minimal summa, komissiya)
    INFO_BLOK = (AppiumBy.ACCESSIBILITY_ID, "Минимал сумма $ 100 \nКомиссия 0%\n$ 100 = ₽ 9 178")

    # Summa input
    SUMMA_INPUT = (AppiumBy.CLASS_NAME, "android.widget.EditText")

    # Valyuta tanlash
    VALYUTA = (AppiumBy.ACCESSIBILITY_ID, "Валюта\nUSD")

    # Davom etish tugmasi
    DAVOM_ETISH = (AppiumBy.ACCESSIBILITY_ID, "Давом этиш")

    # Ortga tugmasi (chap yuqori)
    ORTGA = (AppiumBy.XPATH, '//android.widget.ImageView[@clickable="true" and @bounds="[8,57][104,153]"]')

    # OK 
    XATO_OK = (AppiumBy.ACCESSIBILITY_ID, "Ок")

    # Valyuta tugmalari
    RUB = (AppiumBy.ACCESSIBILITY_ID, "RUB")
    USD = (AppiumBy.ACCESSIBILITY_ID, "USD")

    def select_rub(self):
        """RUB valyutasini tanlaydi."""
        self.click(self.RUB)

    def select_usd(self):
        """USD valyutasini tanlaydi."""
        self.click(self.USD)

    def is_naqd_pul_page(self) -> bool:
        """Naqd pul yuborish sahifasi ochilganini tekshiradi."""
        try:
            self.wait.until(
                lambda d: d.find_element(*self.SARLAVHA)
            )
            return True
        except Exception:
            return False

    def enter_summa(self, summa: str):
        """Summani kiritadi."""
        self.click(self.SUMMA_INPUT)
        self.send_keys(self.SUMMA_INPUT, summa)

    def tap_valyuta(self):
        """Valyuta tanlash tugmasini bosadi."""
        self.click(self.VALYUTA)

    def tap_davom_etish(self):
        """Davom etish tugmasini bosadi."""
        self.click(self.DAVOM_ETISH)

    def tap_ortga(self):
        """Ortga tugmasini bosadi."""
        self.click(self.ORTGA)

    def tap_ok(self):
        self.click(self.XATO_OK)

    def enter_summa(self, summa: str):
        """Summani kiritadi - avval tozalab, keyin yozadi."""
        element = self.driver.find_element(*self.SUMMA_INPUT)
        element.click()
        element.clear()
        element.send_keys(summa)

    