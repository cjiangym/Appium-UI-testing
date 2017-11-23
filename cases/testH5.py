from appium import webdriver
import unittest
import time
from common.common_method import Common_method

class H5Test(unittest.TestCase):
    common_method = Common_method()
    def setUp(self):
        self.driver = self.common_method.setUp()
        time.sleep(3)
    def tearDown(self):
        self.driver.quit()

    def test_dailySign(self):
        u"测试跳转到每日签到ht"
        result = False
        try:
            self.common_method.init_case()
            self.common_method.pop_ads()
            self.driver.find_element_by_id("com.ismartgo.apppub:id/img_msg").click()
            x1 = self.driver.find_element_by_id("com.ismartgo.apppub:id/layout_select_city").size["width"]
            x = self.driver.find_element_by_id("com.ismartgo.apppub:id/layout_new_search").size["width"]
            y1 = self.driver.find_element_by_id("com.ismartgo.apppub:id/imgv_new_msg").size["height"]
            y = self.driver.find_element_by_id("com.ismartgo.apppub:id/rl_top_group").size["height"]
            self.driver.tap([(x1+x,y1+y)],duration=None)                        #计算出屏幕点击区域
            time.sleep(5)
            contexts = self.driver.contexts
            pageName = self.driver.find_element_by_id("com.ismartgo.apppub:id/tv_title").text
            self.assertEqual(pageName,"每日签到")
            self.driver.find_element_by_id("com.ismartgo.apppub:id/tv_left").click()
        except:
            self.common_method.cutScreenShot ("test_search_01" + "_" + self.common_method.timestamp)  # 异常后截图放在erroScreenShot文件夹下
            self.assertEqual (result, "执行失败，请查看截图")

