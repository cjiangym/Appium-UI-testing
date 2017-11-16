from appium import webdriver

desired_caps = {
    "platformName": "Android",
    "deviceName": "N2FGK16816810545",
    "platformVersion": "4.4.4",
    "appPackage": "com.ismartgo.apppub",
    "appActivity": "com.ismartgo.app.activity.WelcomeActivity",
    "unicodeKeyboard": True,
    "resetKeyboard": True
}
driver = webdriver.Remote ('http://127.0.0.1:4723/wd/hub', desired_caps)