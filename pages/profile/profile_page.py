from appium.webdriver.common.appiumby import AppiumBy
from pages.base.base_page import BasePage

class ProfilePage(BasePage):

    #  Settings
    PRIVATE = (AppiumBy.ACCESSIBILITY_ID, "Шахсий маълумотлар")
    SECURITY = (AppiumBy.ACCESSIBILITY_ID, "Хавфсизлик")
    THEME = (AppiumBy.ACCESSIBILITY_ID, "Мавзу")
    LANGUAGE = (AppiumBy.ACCESSIBILITY_ID, "Тилни ўзгартириш")

    # Boshqalar
    PUNKT = (AppiumBy.ACCESSIBILITY_ID, "Пунктлар")
    PROG = (AppiumBy.ACCESSIBILITY_ID, "Иловани баҳолаш")
    SAVOL = (AppiumBy.ACCESSIBILITY_ID, "Кўп бериладиган саволлар")
    OFERT = (AppiumBy.ACCESSIBILITY_ID, "Оммавий офферта")
    ULASH = (AppiumBy.ACCESSIBILITY_ID, "Улашиш")

    # # # # #
    
    

    def click_private(self):
        self.click(self.PRIVATE)

    def click_security(self):
        self.click(self.SECURITY)

    def click_theme(self):
        self.click(self.THEME)

    def click_language(self):
        self.click(self.LANGUAGE)

    # === Boshqalar Methods ===
    def click_punkt(self):
        self.click(self.PUNKT)

    def click_prog(self):
        self.click(self.PROG)

    def click_savol(self):
        self.click(self.SAVOL)

    def click_ofert(self):
        self.click(self.OFERT)

    def click_ulash(self):
        self.click(self.ULASH)
