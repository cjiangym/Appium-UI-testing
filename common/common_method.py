import unittest
import time
import sys
import os
import platform

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.support.wait import WebDriverWait
from appium import webdriver



#用于命令行执行时对所有路径进行搜索（pydev在运行时会把当前工程的所有文件夹路径都作为包的搜索路径，而命令行默认只是搜索当前路径）
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)


class Common_method():
    testTime = time.strftime("%Y-%m-%d", time.localtime())   #测试报告时间
    #timestamp = time.strftime("%Y%m%d %H%M%S")

    # --------初始化----------------#
    def setUp(self):
        desired_caps = {
            "platformName": "Android",
            "deviceName": "A7J5T15509004553",
            "platformVersion": "6.0",
            "appPackage": "com.ismartgo.apppub",
            "appActivity": "com.ismartgo.app.activity.WelcomeActivity",
            "unicodeKeyboard": True,  # ------屏蔽软键盘------
            "resetKeyboard": True,
            "automationName": 'Uiautomator2',

        }
        self.driver = webdriver.Remote ('http://127.0.0.1:4723/wd/hub', desired_caps)
        time.sleep (2)
        return self.driver

    # -----检查是否有开屏广告--------------#
    def adpass(self,driver):
        try:
            driver.wait_activity ("com.ismartgo.app.activity.SmartGoSplashADActivity", 3, 1)
            driver.find_element_by_id('com.ismartgo.apppub:id/tv_countdown').click ()
            time.sleep(2)
        except:
            pass

    # --------检查是否有弹窗广告----------#
    def pop_ads(self,driver):
        try:
            el = driver.find_element_by_id("com.ismartgo.apppub:id/rl_content")       #检查是否有弹窗广告
            x = driver.get_window_size()["width"]
            y = driver.get_window_size()["height"]
            self.driver.tap([(x/2, y-120)], duration=None)                                # 关闭弹窗个广告
            time.sleep(1)
        except:
            pass

    #--------屏幕上滑动-------------#
    def swipe_up(self,driver,t,n):
        window_size = self.driver.get_window_size()
        x0= window_size["width"] *0.5
        y0= window_size["height"] *0.5
        y1= window_size["height"] *0.25
        for i in range(n):
            self.driver.swipe(x0,y0,x0,y1,t)

    # --------屏幕左滑动-------------#
    def swipe_left(self, driver, t, n):
        window_size = self.driver.get_window_size ()
        x0 = window_size["width"] * 0.5
        y0 = window_size["height"] * 0.5
        x1 = window_size["width"] * 0.25
        for i in range (n):
            self.driver.swipe (x0, y0, x1, y0, t)

    # --------屏幕右滑滑动-------------#
    def swipe_right(self, driver, t, n):
        window_size = self.driver.get_window_size()
        x0 = window_size["width"] * 0.5
        y0 = window_size["height"] * 0.5
        x1 = window_size["width"] * 0.75
        for i in range (n):
            self.driver.swipe (x0, y0, x1, y0, t)



    #-----------截图路径--------------#
    def cutScreenShot(self,driver,picName):
        fileName = rootPath + "\\errorScreenShot\\" + picName + ".png"  #将用例方法名作为图片名
        driver.get_screenshot_as_file(fileName)
        time.sleep(2)
        return fileName

    #----------获取测试报告----------#
    def get_reportpath(self):
        report_path = rootPath + "\\report\\" + self.testTime + "-testResult.html"
        return report_path

    '''判断toast是否存在
    def is_toast_exist(self,driver,text,timeout =30,poll_frequency=0.5):
        try:
            toast_loc = ("xpath", ".//*[contains(@text,'%s')]" % text)
            WebDriverWait(driver,timeout,poll_frequency).until(EC.presence_of_element_located(toast_loc))
            #WebDriverWait (driver, timeout, poll_frequency).until(EC.presence_of_element_located((By.XPATH, toast_loc)))
            return True
        except:
           return False
    '''