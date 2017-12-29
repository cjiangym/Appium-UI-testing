#coding:utf-8

from appium import webdriver
import unittest
import time
from common.common_method import Common_method

class LoginTest(unittest.TestCase):
    common_method = Common_method()

    def setUp(self):
        self.driver = self.common_method.setUp()
        time.sleep(3)
    def tearDown(self):
        self.driver.quit()

    def test_phoneLogin(self):
        u"测试手机号码登录"
        try:
            self.common_method.adpass(self.driver)
            self.common_method.pop_ads(self.driver)
            self.driver.find_element_by_name("我").click()
            self.driver.find_element_by_class_name("android.widget.ImageView").click()
            self.driver.find_element_by_id("com.ismartgo.apppub:id/et_phone").send_keys("16666666339")
            self.driver.find_element_by_id("com.ismartgo.apppub:id/layout_password_input").send_keys("123456")
            self.driver.find_element_by_id("com.ismartgo.apppub:id/btn_login").click()
            self.driver.wait_activity("com.ismartgo.app.activity.Tab_Container_Activity",timeout=8,interval=1)
            text = self.driver.find_element_by_id("com.ismartgo.apppub:id/tv_sign_days").text
            self.assertIn("连续签到",text)
        except Exception as a:
            self.common_method.cutScreenShot(self.driver,"手机号登录")
            self.assertTrue(None,"执行失败，请查看截图")
