import unittest
import time
import sys
import os
import platform
from appium import webdriver
#用于命令行执行时对所有路径进行搜索（pydev在运行时会把当前工程的所有文件夹路径都作为包的搜索路径，而命令行默认只是搜索当前路径）
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)


class Common_method():
    testTime = time.strftime("%Y-%m-%d", time.localtime())   #测试报告时间
    timestamp = time.strftime("%Y%m%d %H%M%S")
    #获取测试报告
    def get_reportpath(self):
        report_path = rootPath + "\\report\\" + self.testTime + "-testResult.html"
        return report_path

        # -----用例初始化,检查开屏广告--------------#
    def init_case(self):
        try:
            time.sleep (1)
            el = self.driver.find_element_by_id("com.ismartgo.apppub:id/iv_ad_top")  # 获取开屏广告是否存在
            self.driver.find_element_by_id ("com.ismartgo.apppub:id/tv_countdown").click ()  # 点击开屏广告上的'点击跳过'按钮
            time.sleep (2)
        except:
            pass

    # --------检查弹窗广告----------------#
    def pop_ads(self):
        try:
            time.sleep(2)
            el = self.driver.find_element_by_id("com.ismartgo.apppub:id/rl_content")       #检查是否有弹窗广告
            x = self.driver.get_window_size()["width"]
            y = self.driver.get_window_size()["height"]
            self.driver.tap ([(x/2, y-120)], duration=None)  # 关闭弹窗个广告
            time.sleep(2)
        except:
            pass

    def setUp(self):
        desired_caps = {
            "platformName": "Android",
            "deviceName": "N2FGK16816810545",
            "platformVersion": "4.4.4",
            "appPackage": "com.ismartgo.apppub",
            "appActivity": "com.ismartgo.app.activity.WelcomeActivity",
            "unicodeKeyboard": True,
            "resetKeyboard": True
        }
        self.driver = webdriver.Remote ('http://127.0.0.1:4723/wd/hub', desired_caps)
        time.sleep (2)
        return self.driver

    #-----------截图路径--------------#
    def cutScreenShot(self,picName):
        fileName = rootPath + "\\errorScreenShot\\" + picName + ".png"  #将用例方法名作为图片名
        self.driver.get_screenshot_as_file(fileName)
        time.sleep(2)