import pathlib

# Appiumサーバへの接続情報
APPIUM_SERVER = "http://127.0.0.1:4723/wd/hub"
# テストするアプリのapkファイルパス
ANDROID_APP_PATH = "./app-debug.apk"
# スクリーンショットの保存先
SCREENSHOTS_DIR = "screenshots"

# desired capabilities(common)
def get_desired_capabilities_base():
  caps = {}

  caps["appium:ensureWebviewsHavePages"] = True
  # スクリーンショット有効
  caps["appium:nativeWebScreenshot"] = True
  caps["appium:newCommandTimeout"] = 3600
  caps["appium:connectHardwareKeyboard"] = True

  return caps

# desired capabilities for android
def get_desired_capabilities_android():
  appPath = str(pathlib.Path(ANDROID_APP_PATH).resolve())
  
  caps = get_desired_capabilities_base()
  caps["platformName"] = "android"

  # If launch app already installed, specify appPackage and activity
  # caps["appium:appPackage"] = ANDROID_APP_PACKAGE
  # caps["appium:appActivity"] = ANDROID_APP_ACTIVITY

  # If re-install app before test, specify app path
  # 以下の設定で、テスト毎にアプリを再インストール
  caps["app"] = appPath
  caps["allowTestPackages"] = True  # True: package for simulator
  caps["enforceAppInstall"] = True  # re-install app before test

  return caps
