from appium.webdriver.common.appiumby import AppiumBy
import appium
from appium import webdriver
import pytest

android_caps = {"appium:deviceName": "Pixel 6 API 33",
                "platformName": "Android",
                "appium:app": "/Users/firuzkhodjaev/PycharmProjects/ipoteka_mobile_autotest/apps/IpotekaBank.apk",
                "appium:noReset": True,
                "appium:automationName": "UiAutomator2",
                "appium:ensureWebviewsHavePages": True,
                "appium:nativeWebScreenshot": True,
                "appium:newCommandTimeout": 3600,
                "appium:connectHardwareKeyboard": True
                }

appium_server_url = 'http://localhost:4723/wd/hub'


@pytest.fixture()
def mobile_driver():
    driver = appium.webdriver.Remote(appium_server_url, android_caps)
    yield driver
    driver.quit()