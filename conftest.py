import pytest
import time
import os
from datetime import datetime
from dotenv import load_dotenv
from appium import webdriver
from appium.options.android import UiAutomator2Options

load_dotenv()

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    
    if rep.when == "call" and rep.failed:
        driver = item.funcargs.get("driver")
        if driver:
            try:
                os.makedirs("screenshots", exist_ok=True)
                timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
                test_name = item.name
                path = f"screenshots/{test_name}_{timestamp}.png"
                driver.save_screenshot(path)
                print(f"\n Screenshot saqlandi: {path}")
            except Exception as e:
                print(f"\n Screenshot olinmadi: {e}")


@pytest.fixture(scope="function")
def driver():
    options = UiAutomator2Options()

    options.platform_name = "Android"
    options.automation_name = "UiAutomator2"
    options.device_name = "Android"
    options.udid = os.getenv("UDID")

    options.app_package = os.getenv("APP_PACKAGE")
    options.app_activity = ".MainActivity"

    options.no_reset = True
    options.full_reset = False

    driver = webdriver.Remote("http://127.0.0.1:4723", options=options)
    driver.implicitly_wait(15)

    driver.terminate_app(os.getenv("APP_PACKAGE"))
    time.sleep(2)
    driver.activate_app(os.getenv("APP_PACKAGE"))
    time.sleep(5)

    yield driver

    # driver.terminate_app(os.getenv("APP_PACKAGE"))