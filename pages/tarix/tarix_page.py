from appium.webdriver.common.appiumby import AppiumBy
from pages.base.base_page import BasePage


class TarixPage(BasePage):

    DAVR = (AppiumBy.ACCESSIBILITY_ID, "Давр")
    OTKAZMA_TURI = (AppiumBy.ACCESSIBILITY_ID, "Ўтказма тури")
    HAFTA = (AppiumBy.ACCESSIBILITY_ID, "Ҳафта")
    OY = (AppiumBy.ACCESSIBILITY_ID, "Ой")
    YIL = (AppiumBy.ACCESSIBILITY_ID, "Йил")
    DAVR_ORALIGINI_KIRITISH = (AppiumBy.ACCESSIBILITY_ID, "Давр оралиғини киритиш")

    def is_tarix_page(self):
        try:
            self.wait.until(
                lambda d: d.find_element(
                    AppiumBy.ACCESSIBILITY_ID, "Тарих")
            )
            return True
        except:
            return False

    def scroll_to_bottom(self):
        self.driver.find_element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiScrollable(new UiSelector().scrollable(true)).scrollToEnd(10)'
        )

    def scroll_to_top(self):
        self.driver.find_element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiScrollable(new UiSelector().scrollable(true)).scrollToBeginning(10)'
        )

    def tap_davr(self):
        self.click(self.DAVR)
    
    def tap_otkazma_turi(self):
        self.click(self.OTKAZMA_TURI)

    def tap_hafta(self):
        self.click(self.HAFTA)

    def tap_oy(self):
        self.click(self.OY)

    def tap_yil(self):
        self.click(self.YIL)

    def tap_davr_oraligini_kiritish(self):
        self.click(self.DAVR_ORALIGINI_KIRITISH)