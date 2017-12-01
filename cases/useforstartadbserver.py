from appium import webdriver

desired_caps = {
    "platformName": "Android",
    "deviceName": "A7J5T15509004553",
    "platformVersion": "6.0",
    "appPackage": "com.ismartgo.apppub",
    "appActivity": "com.ismartgo.app.activity.WelcomeActivity",
    "unicodeKeyboard": True,
    "resetKeyboard": True,
    "noReset":True
}
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
driver.quit()

'''
"deviceName": "a010f1d5",
"platformVersion": "7.0",

    "deviceName": "N2FGK16816810545",
    "platformVersion": "4.4.4",
'''

