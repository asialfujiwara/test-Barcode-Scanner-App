# This sample code uses the Appium python client v2
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python

from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

import pytest
import sys
import pathlib
import util
from time import sleep

DEVICE_NAME = "Pixel_5_API_31"

testName = pathlib.Path(__file__).stem
screenShotsBase = util.SCREENSHOTS_DIR + "/" + testName

@pytest.fixture
def fixture_driver():
  # setup(before test) 
  caps = util.get_desired_capabilities_android()
  caps["appium:avd"] = DEVICE_NAME

  # start appium session
  return webdriver.Remote(util.APPIUM_SERVER, caps)

def test_from_launch_to_check_timeout_prompt(fixture_driver):
  settings = {
    'screenShotsBase': screenShotsBase + '_' + sys._getframe().f_code.co_name,
    'cameraArrowButtonId': "com.android.permissioncontroller:id/permission_allow_foreground_only_button"
  }

  # launch
  # スクリーンショット1枚目 - アプリ起動直後
  sleep(5)
  fixture_driver.save_screenshot(settings['screenShotsBase'] + "_01.png")

  # "スキャンする" をタップ
  el1 = fixture_driver.find_element(by=AppiumBy.XPATH, value="//*[@resource-id='scan']")
  el1.click()

  # カメラの使用を許可
  sleep(2)
  fixture_driver.save_screenshot(settings['screenShotsBase'] + "_02.png")
  # カメラの許可をタップ
  el2 = fixture_driver.find_element(by=AppiumBy.ID, value=settings['cameraArrowButtonId'])
  el2.click()

  # scanner screen
  sleep(10)
  fixture_driver.save_screenshot(settings['screenShotsBase'] + "_03.png")

  # check timeout prompt
  el3 = fixture_driver.find_elements(by=AppiumBy.ID, value="com.example.helloworld:id/timeout_prompt")
  # メッセージ文字列が一致すればテストSUCCESS
  assert len(el3) > 0 and el3[0].text == "Not detected"

  # quit
  fixture_driver.quit()
