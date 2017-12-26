# coding :utf-8

from appium import webdriver
import unittest
import time
from common.common_method import Common_method

class SearchTest(unittest.TestCase):
    common_method = Common_method()

    def setUp(self):
        self.driver = self.common_method.setUp()
        time.sleep(3)

    def tearDown(self):
        self.driver.quit()

    def test_search_01(self):                    #Edit by Cjiang 2017.11.15
        u"测试搜索商店"
        try:
            self.common_method.adpass(self.driver)
            self.common_method.pop_ads(self.driver)
            self.driver.find_element_by_id("com.ismartgo.apppub:id/layout_new_search").click()
            self.driver.find_element_by_id("com.ismartgo.apppub:id/layout_search").send_keys(u"沃尔玛")
            self.driver.find_element_by_id("com.ismartgo.apppub:id/tv_search").click()
            self.driver.implicitly_wait(8)
            text = self.driver.find_element_by_id("com.ismartgo.apppub:id/tbutton").text
            self.assertEqual(text,"附近")
            result = True
        except:
            self.common_method.cutScreenShot(self.driver,"搜索商店")               #异常后截图放在erroScreenShot文件夹下
            self.assertEqual(None,"执行失败，请查看截图")


    def test_search_02(self):
        u"测试搜索商品"
        try:
            self.common_method.adpass(self.driver)
            self.common_method.pop_ads(self.driver)
            self.driver.find_element_by_id("com.ismartgo.apppub:id/layout_new_search").click()
            self.driver.find_element_by_id("com.ismartgo.apppub:id/layout_search").send_keys(u"立白")
            self.driver.find_element_by_id("com.ismartgo.apppub:id/tv_search").click()
            self.driver.implicitly_wait(8)
            text = self.driver.find_element_by_name("附近优惠").text
            self.assertEqual (text, "附近优惠")
        except:
            self.common_method.cutScreenShot(self.driver,"搜索商品")                           #异常后截图放在erroScreenShot文件夹下
            self.assertTrue(None,"执行失败，请查看截图")
