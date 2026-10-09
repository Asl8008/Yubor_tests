from appium.webdriver.common.appiumby import AppiumBy
from pages.base.base_page import BasePage
import time


class KartagaPage(BasePage):

    # Davlatlar
    OZBEKISTON = (AppiumBy.ACCESSIBILITY_ID, "Ўзбекистон")
    TOJIKISTON = (AppiumBy.ACCESSIBILITY_ID, "Тожикистон")
    QIRGIZISTON = (AppiumBy.ACCESSIBILITY_ID, "Қирғизистон")

    # Yuborish turi 
    KARTAGA_YUBORISH_TURI = (AppiumBy.ACCESSIBILITY_ID, "Картага юбориш")
    TELEFON_ORQALI = (AppiumBy.ACCESSIBILITY_ID, "Телефон рақам орқали юбориш")

    # Karta orqali sahifa
    KARTA_INPUT = (AppiumBy.CLASS_NAME, "android.widjet.EditText")
    DAVOM_ETISH = (AppiumBy.ACCESSIBILITY_ID, "Давом этиш")



    def is_kartaga_page(self) -> bool:
        try:
            self.wait.until(
                lambda d: d.find_element(AppiumBy.ACCESSIBILITY_ID, "Қабул қилувчи давлат")
            )
            return True
        except:
            return False

    def select_ozbekiston(self):
        self.click(self.OZBEKISTON)

    def select_tojikiston(self):
        self.click(self.TOJIKISTON)

    def select_qirgiziston(self):
        self.click(self.QIRGIZISTON)

    def is_yuborish_turi_page(self) -> bool:
        try:
            self.wait.until(
                lambda d: d.find_element(AppiumBy.ACCESSIBILITY_ID, "Юбориш турини танланг")
            )
            return True
        except:
            return False
        
    def select_kartaga_yuborish(self):
        self.click(self.KARTAGA_YUBORISH_TURI)
    
    def select_telefon_orqali(self):
        self.click(self.TELEFON_ORQALI)

    def is_karta_orqali_page(self) -> bool:
        try:
            self.wait.until(
                lambda d: d.find_element(AppiumBy.ACCESSIBILITY_ID, "Карта орқали")
            )
            return True
        except:
            return False

    def enter_card_number(self, card_number: str):
        input_field = self.driver.find_element(AppiumBy.CLASS_NAME, "android.widget.EditText")
        input_field.click()
        time.sleep(1)
        input_field.send_keys(card_number)

    def tap_davom_etish(self):
        # self.driver.hide_keyboard()
        time.sleep(1)
        self.click(self.DAVOM_ETISH)    