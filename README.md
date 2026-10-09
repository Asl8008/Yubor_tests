# Yubor Mobile Automation Tests

Yubor ilovasi (`uz.yubor.app`) uchun Appium va Pytest yordamida yozilgan avtomatlashtirilgan testlar to'plami.

## Texnologiyalar
- **Python 3**
- **Appium** (Appium-Python-Client)
- **Pytest**
- **Selenium WebDriver**
- **Page Object Model (POM)** pattern
- **python-dotenv**

## Sozlash va O'rnatish

1. Virtual muhit yaratish va faollashtirish:
```bash
python3 -m venv .venv
source .venv/bin/activate
```

2. Kerakli kutubxonalarni o'rnatish:
```bash
pip install -r requirements.txt
```

3. Muhit o'zgaruvchilarini sozlash:
`.env.example` faylidan nusxa olib, `.env` faylini yarating va qurilma ma'lumotlarini kiriting:
```bash
cp .env.example .env
```

## Testlarni ishga tushirish

1. Appium serverini ishga tushiring:
```bash
appium
```

2. Testlarni bajarish:
```bash
pytest
```
