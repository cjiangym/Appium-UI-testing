# coding :utf-8
from appium import webdriver
import unittest
import time
from common.common_method import Common_method

class HomepageTest(unittest.TestCase):
    common_method = Common_method()

    def setUp(self):
        self.driver = self.common_method.setUp()
        time.sleep (5)
    def tearDown(self):
        pass

    def test_ClickShopSign(self):
        u"测试到店签到"
        try:
            self.common_method.init_case()                       #判断开屏广告
            self.driver.find_element_by_name("到店签到").click()
            time.sleep (5)
            pageName = self.driver.find_element_by_id("com.ismartgo.apppub:id/tv_title").text
            self.assertEqual(pageName,"到店签到")
            self.driver.find_element_by_id("com.ismartgo.apppub:id/pv_back").click()
        except:
            self.common_method.cutScreenShot("test_ClickShopSign")