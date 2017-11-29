# coding :utf-8
from appium import webdriver
import unittest
import time
from common.common_method import Common_method

class HomepageTest(unittest.TestCase):
    common_method = Common_method()

    def setUp(self):
        self.driver = self.common_method.setUp()
        time.sleep(3)
    def tearDown(self):
        self.driver.quit()

    def test_recommendation_nearby_01(self):
        u"测试首页推荐 - 附近推荐，点击左边图片"
        result = False
        try:
            self.common_method.adpass (self.driver)
            self.common_method.pop_ads (self.driver)
            self.driver.find_element_by_id("com.ismartgo.apppub:id/iv_left_img").click()
            time.sleep(1)
        except Exception as e:
            self.common_method.cutScreenShot ("test_recommendation_nearby_01" + "_" + self.common_method.timestamp)
            self.assertEqual(result, "执行失败，请查看截图")
        self.assertEqual(self.driver.current_activity,"com.ismartgo.app.activity.SearchForPromotionNewActivity")
        self.driver.find_element_by_id("com.ismartgo.apppub:id/pv_back").click()
        self.assertEqual(self.driver.current_activity, "com.ismartgo.app.activity.Tab_Container_Activity")

    def test_recommendation_nearby_02(self):
        u"测试首页推荐 - 附近推荐，点击右上角图片"
        result = False
        try:
            self.common_method.adpass (self.driver)
            self.common_method.pop_ads (self.driver)
            self.driver.find_element_by_id("com.ismartgo.apppub:id/iv_right_top_img").click()
            time.sleep(1)
        except Exception as e:
            self.common_method.cutScreenShot ("test_recommendation_nearby_02" + "_" + self.common_method.timestamp)
            self.assertEqual(result, "执行失败，请查看截图")
        self.assertEqual(self.driver.current_activity,"com.ismartgo.app.activity.SearchForPromotionNewActivity")
        self.driver.find_element_by_id("com.ismartgo.apppub:id/pv_back").click()
        self.assertEqual(self.driver.current_activity, "com.ismartgo.app.activity.Tab_Container_Activity")

    def test_recommendation_nearby_03(self):
        u"测试首页推荐 - 附近推荐，点击右下角图片"
        result = False
        try:
            self.common_method.adpass (self.driver)
            self.common_method.pop_ads (self.driver)
            self.driver.find_element_by_id("com.ismartgo.apppub:id/iv_right_bottom_img").click()
            time.sleep(1)
        except Exception as e:
            self.common_method.cutScreenShot ("test_recommendation_nearby_02" + "_" + self.common_method.timestamp)
            self.assertEqual(result, "执行失败，请查看截图")
        self.assertEqual(self.driver.current_activity,"com.ismartgo.app.activity.SearchForPromotionNewActivity")
        self.driver.find_element_by_id("com.ismartgo.apppub:id/pv_back").click()
        self.assertEqual(self.driver.current_activity, "com.ismartgo.app.activity.Tab_Container_Activity")

    def test_recommendation_shopping_01(self):
        u"测试首页推荐 - 点击网购推荐，点击左边图片"
        result = False
        try:
            self.common_method.adpass (self.driver)
            self.common_method.pop_ads (self.driver)
            self.driver.find_element_by_id("com.ismartgo.apppub:id/tv_tab2").click()
            self.text = self.driver.find_element_by_id("com.ismartgo.apppub:id/tv_recommend_title").text
            self.assertEqual(self.text, "超值推荐")
            self.driver.find_element_by_id("com.ismartgo.apppub:id/tv_recommend_desc").click()
            time.sleep(2)
            self.pageName = self.driver.find_element_by_id("com.ismartgo.apppub:id/tv_title").text
        except Exception as e:
            self.common_method.cutScreenShot ("test_recommendation_shopping_01" + "_" + self.common_method.timestamp)
            self.assertEqual(result, "执行失败，请查看截图")
        self.assertEqual(self.pageName,"规则说明")
        self.driver.find_element_by_id("com.ismartgo.apppub:id/tv_left").click()
        self.assertEqual(self.driver.current_activity, "com.ismartgo.app.activity.Tab_Container_Activity")