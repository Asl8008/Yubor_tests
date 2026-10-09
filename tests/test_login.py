import time
import pytest
import logging
from pages.login.login_page import LoginPage
from pages.otp.otp_page import OtpPage
from pages.pin.pin_page import PinPage
from pages.fingerprint.fingerprint_page import FingerprintPage
from pages.home.home_page import HomePage
from pages.kartaga_yuborish.kartaga_page import KartagaPage
from pages.kartaga_yuborish.summa_page import SummaPage
from pages.kartaga_yuborish.telefon_page import TelefonPage
from pages.tarix.tarix_page import TarixPage
from pages.naqd.naqd_page import NaqdPage
from pages.help.help_page import HelpPage
from pages.profile.profile_page import ProfilePage

logger = logging.getLogger(__name__)

def test_login(driver):
    # # 1. Onboarding + telefon raqam
    # login = LoginPage(driver)
    # login.login("9692803381")

    # time.sleep(2)

    # # 2. OTP kiritish
    # otp = OtpPage(driver)
    # otp.enter_otp("111111")

    # time.sleep(2)

    # 3. PIN kiritish
    pin = PinPage(driver)
    pin.enter_pin("5555")
    time.sleep(2)
    # pin.enter_pin("5555")
    # time.sleep(2)

    # # 4. Barmoq skaneri - o'tkazib yuborish
    # fingerprint = FingerprintPage(driver)
    # fingerprint.skip()
    # time.sleep(2)

 
    # 5. Home page tekshiruvi
    home = HomePage(driver)
    assert home.is_home_page(), "Home page ochilmadi!"

    # home.tap_kartaga_yuborish()
    # time.sleep(3)

    # # 6. Davlatni tanlash
    # kartaga = KartagaPage(driver)
    # assert kartaga.is_kartaga_page(), "Kartaga yuborish sahifasi ochilmadi!"
    # kartaga.select_ozbekiston()
    # time.sleep(2)

    # # 7. Yuborish turini tanlash
    # assert kartaga.is_yuborish_turi_page(), "Yuborish turi sahifasi ochilmadi!"
    # kartaga.select_kartaga_yuborish()
    # time.sleep(2)

    # # 8. Karta raqam kiritish
    # assert kartaga.is_karta_orqali_page(), "Karta orqali sahifasi ochilmadi!"
    # kartaga.enter_card_number("4097830067479135")
    # time.sleep(2)
    # kartaga.tap_davom_etish()
    # time.sleep(2)

    # # 9. Summa kiritish
    # summa = SummaPage(driver)
    # summa.enter_summa("150000")
    # time.sleep(2)
    # summa.tap_davom_etish()
    # time.sleep(2)

    # # 10. Xato - OK bosish
    # summa.tap_ok()
    # time.sleep(2)

    # # 11. Valyuta tanlash - RUB
    # summa.tap_valyuta()
    # time.sleep(2)
    # summa.select_rub()
    # time.sleep(2)

    # # 12. Davom etish
    # summa.tap_davom_etish()
    # time.sleep(2)

    # # 13. Xato - OK bosish
    # summa.tap_ok()
    # time.sleep(2)

    # # 14. Orqaga 2 marta
    # driver.back()
    # time.sleep(1)
    # driver.back()
    # time.sleep(1)

    # # 15. Telefon raqam orqali yuborish
    # kartaga.select_telefon_orqali()
    # # home.tap_naqd_pul_yuborish()
    # time.sleep(2)

    # # 16. Telefon raqam kiritish
    # telefon = TelefonPage(driver)
    # telefon.enter_phone("886118008")
    # time.sleep(2)

    # # 17. Bank tanlash - Hamkorbank
    # telefon.tap_bank_tanlang()
    # time.sleep(2)
    # telefon.select_hamkorbank()
    # time.sleep(2)

    # # 18. Davom etish
    # telefon.tap_davom_etish()
    # time.sleep(2)

    # # 19. Summa kiritish
    # summa2 = SummaPage(driver)
    # summa2.enter_summa("150000")
    # time.sleep(2)
    # summa2.tap_davom_etish()
    # time.sleep(2)

    # # 20. Xato - OK
    # summa2.tap_ok()
    # time.sleep(2)

    # # 21. Valyuta - RUB
    # summa2.tap_valyuta()
    # time.sleep(2)
    # summa2.select_rub()
    # time.sleep(2)

    # # 22. Davom etish
    # summa2.tap_davom_etish()
    # time.sleep(2)

    # # 23. Xato - OK
    # summa2.tap_ok()
    # time.sleep(2)

    # # 23. Orqaga 3 marta
    # driver.back()
    # time.sleep(1)
    # driver.back()
    # time.sleep(1)
    # driver.back()
    # time.sleep(1)

    # # 24. Tojikiston
    # kartaga2 = KartagaPage(driver)
    # kartaga2.select_tojikiston()
    # time.sleep(2)
    # driver.back()
    # time.sleep(1)

    # # 25. Qirgiziston
    # kartaga2.select_qirgiziston()
    # time.sleep(2)
    # driver.back()
    # time.sleep(1)
    # driver.back()
    # time.sleep(1)

    # # 26. Home pageda
    # assert home.is_home_page(), "Home page ochilmadi!"

    # # 27. Naqd pul yuborish
    # home.tap_naqd_pul_yuborish()
    # time.sleep(2)

    # naqd = NaqdPage(driver)
    # naqd.enter_summa("100")
    # naqd.tap_davom_etish()
    # time.sleep(2)

    # naqd.tap_ok()
    # time.sleep(2)

    # # Valyuta - RUB
    # naqd.tap_valyuta()
    # time.sleep(2)
    # naqd.select_rub()
    # time.sleep(2)

    # naqd.enter_summa("1000")
    # time.sleep(2)

    # naqd.tap_davom_etish()
    # naqd.tap_ok()
    # time.sleep(2)

    # driver.back()
    # time.sleep(3)


    # home scroll
    # home.scroll_bottom()


    # # 28. Tarix
    # time.sleep(2)
    # home.go_to_tarix()
    # time.sleep(2)

    # tarix = TarixPage(driver)
    # assert tarix.is_tarix_page(), "Tarix sahifasi ochilmadi!"

    # # Pastga scroll
    # tarix.scroll_to_bottom()
    # time.sleep(2)

    # # Yuqoriga qaytsh
    # tarix.scroll_to_top()
    # time.sleep(2)

    # # Davr bosish
    # tarix.tap_davr()
    # time.sleep(2)
    # driver.back()
    # time.sleep(2)

    # # O'tkazma turi
    # tarix.tap_otkazma_turi()
    # time.sleep(2)
    # driver.back()
    # time.sleep(1)
    # driver.back()


    # tarix.tap_davr()
    # time.sleep(2)

    # # Hafta
    # tarix.tap_hafta()
    # time.sleep(2)

    # # Oy
    # tarix.tap_oy()
    # time.sleep(2)

    # # Yil
    # tarix.tap_yil()
    # time.sleep(2)

    # # Davr oraligini kiritish
    # tarix.tap_davr_oraligini_kiritish()
    # time.sleep(2)

    # O'tkazishga kirish
    # home = HomePage(driver)
    # home.go_to_otkazish()
    # time.sleep(2)

    # home.go_to_yordam()
    # time.sleep(2)

    # help = HelpPage(driver)
    # help.tap_onlayn_chat()
    # time.sleep(5)
    # driver.back()
    # help.tap_telegram()
    # time.sleep(5)
    # driver.back()
    # help.tap_elektron_pochta()
    # time.sleep(5)

    # driver.back()
    # time.sleep(1)
    # driver.back()
    # time.sleep(1)

    home.go_to_profil()
    time.sleep(2)

    profil = ProfilePage(driver)

    profil.click_security()
    time.sleep(2)
    driver.back()
    time.sleep(1)

    profil.click_theme()
    time.sleep(2)
    driver.back()
    time.sleep(1)

    profil.click_language()
    time.sleep(2)
    driver.back()
    time.sleep(1)

    profil.click_punkt()
    time.sleep(2)
    driver.back()
    time.sleep(1)

    profil.click_prog()
    time.sleep(2)
    driver.back()
    time.sleep(1)

    profil.click_savol()
    time.sleep(2)
    driver.back()
    time.sleep(1)

    profil.click_ofert()
    time.sleep(2)
    driver.back()
    time.sleep(1)

    profil.click_ulash()
    time.sleep(2)
    driver.back()
    time.sleep(1)
