# coding :utf-8
from appium import webdriver
import unittest
import time
from common.common_method import Common_method

class HomepageTest(unittest.TestCase):
    common_method = Common_method()

    def setUp(self):
        self.driver = self.common_method.setUp()
        time.sleep(5)
    def tearDown(self):
        self.driver.quit()

    def test_clickShopSign(self):
        u"测试到店签到"
        result = False
        try:
            self.common_method.init_case()                       #判断开屏广告
            self.common_method.pop_ads()                         #关闭弹窗广告
            self.driver.find_element_by_name("到店签到").click()
            time.sleep (5)
            pageName = self.driver.find_element_by_id("com.ismartgo.apppub:id/tv_title").text
            self.assertEqual(pageName,"到店签到")
            signButton = self.driver.find_element_by_xpath("//android.support.v7.widget.RecyclerView/android.widget.LinearLayout[0]/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.LinearLayout[1]")
            canSign =signButton.is_enabled()
            self.driver.find_element_by_id("com.ismartgo.apppub:id/pv_back").click()
        except:
            self.common_method.cutScreenShot("test_ClickShopSign"+"_"+self.common_method.timestamp)
            self.assertEqual(result,"执行失败，请查看截图")

    def test_clickzbgame(self):
        u"测试拍立赚"
        result = False
        try:
            self.common_method.init_case()                       #判断开屏广告
            self.common_method.pop_ads()                         #关闭弹窗广告
            self.driver.find_element_by_name("拍立赚").click()
            time.sleep (5)
            pageName = self.driver.find_element_by_id("com.ismartgo.apppub:id/rb_all").text
            self.assertEqual(pageName,"全部")
            self.driver.find_element_by_id("com.ismartgo.apppub:id/tv_left").click()
        except:
            self.common_method.cutScreenShot("test_ClickShopSign"+"_"+self.common_method.timestamp)
            self.assertEqual(result,"执行失败，请查看截图")

    def test_clickreceipt(self):
        u"测试上传小票功能按钮"
        result = False
        try:
            self.common_method.init_case()                       #判断开屏广告
            self.common_method.pop_ads()                         #关闭弹窗广告
            self.driver.find_element_by_name("小票记账").click()
            time.sleep(5)
            self.driver.find_element_by_id("com.ismartgo.apppub:id/iv_receipt_back").click()
        except:
            self.common_method.cutScreenShot("test_ClickShopSign"+"_"+self.common_method.timestamp)
            self.assertEqual(result,"执行失败，请查看截图")