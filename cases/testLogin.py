#coding:utf-8

from appium import webdriver
import unittest
import time
from common.common_method import Common_method

class LoginTest(unittest.TestCase):

    def setUp(self):
        self.driver = Common_method.setUp(self)
        time.sleep(5)
    def tearDown(self):
        self.driver.quit()

    def test_phoneLogin(self):
        u"测试手机号码登录"
        result = False
        try:
            Common_method.init_case(self)
            Common_method.pop_ads(self)
            self.driver.find_element_by_name("我").click()
            self.driver.find_element_by_class_name("android.widget.ImageView").click()
            self.driver.find_element_by_id("com.ismartgo.apppub:id/et_phone").send_keys("13450244170")
            self.driver.find_element_by_id("com.ismartgo.apppub:id/layout_password_input").send_keys("123456")
            self.driver.find_element_by_id("com.ismartgo.apppub:id/btn_login").click()
            time.sleep(5)
            text = self.driver.find_element_by_id("com.ismartgo.apppub:id/tv_sign_days").text
            self.assertIn("连续签到",text)
        except Exception as a:
            Common_method.cutScreenShot("手机号登录"+"_"+Common_method.timestamp)
            self.assertTrue(result,"执行失败，请查看截图")
