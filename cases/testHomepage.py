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
        try:
            self.common_method.adpass (self.driver)
            self.common_method.pop_ads (self.driver)
            self.driver.find_element_by_id("com.ismartgo.apppub:id/iv_left_img").click()
            self.driver.implicitly_wait(8)
        except Exception as e:
            self.common_method.cutScreenShot(self.driver,"附近推荐-点击左边图片")
            self.assertEqual(None, "执行失败，请查看截图")
        self.assertEqual(self.driver.current_activity,"com.ismartgo.app.activity.SearchForPromotionNewActivity")
        self.driver.implicitly_wait(8)
        self.driver.find_element_by_id("com.ismartgo.apppub:id/pv_back").click()
        self.assertEqual(self.driver.current_activity, "com.ismartgo.app.activity.Tab_Container_Activity")

    def test_recommendation_nearby_02(self):
        u"测试首页推荐 - 附近推荐，点击右上角图片"
        try:
            self.common_method.adpass (self.driver)
            self.common_method.pop_ads (self.driver)
            self.driver.find_element_by_id("com.ismartgo.apppub:id/iv_right_top_img").click()
            time.sleep(1)
        except Exception as e:
            self.common_method.cutScreenShot (self.driver,"附近推荐-点击右上角图片" )
            self.assertEqual(None, "执行失败，请查看截图")
        self.assertEqual(self.driver.current_activity,"com.ismartgo.app.activity.SearchForPromotionNewActivity")
        time.sleep(1)
        self.driver.find_element_by_id("com.ismartgo.apppub:id/pv_back").click()
        self.assertEqual(self.driver.current_activity, "com.ismartgo.app.activity.Tab_Container_Activity")

    def test_recommendation_nearby_03(self):
        u"测试首页推荐 - 附近推荐，点击右下角图片"
        try:
            self.common_method.adpass (self.driver)
            self.common_method.pop_ads (self.driver)
            self.driver.find_element_by_id("com.ismartgo.apppub:id/iv_right_bottom_img").click()
            self.driver.implicitly_wait(8)
        except Exception as e:
            self.common_method.cutScreenShot(self.driver,"附近推荐-点击右下角图片")
            self.assertEqual(None, "执行失败，请查看截图")
        self.assertEqual(self.driver.current_activity,"com.ismartgo.app.activity.SearchForPromotionNewActivity")
        time.sleep(1)
        self.driver.find_element_by_id("com.ismartgo.apppub:id/pv_back").click()
        self.assertEqual(self.driver.current_activity, "com.ismartgo.app.activity.Tab_Container_Activity")

    def test_recommendation_shopping_01(self):
        u"测试首页推荐 - 点击网购推荐"
        try:
            self.common_method.adpass(self.driver)
            self.common_method.pop_ads(self.driver)
            self.driver.find_element_by_id("com.ismartgo.apppub:id/tv_tab2").click()
            self.text = self.driver.find_element_by_id("com.ismartgo.apppub:id/tv_recommend_title").text
            self.assertEqual(self.text, "超值推荐")
            self.driver.find_element_by_id("com.ismartgo.apppub:id/tv_recommend_desc").click()
            self.driver.implicitly_wait(10)
            self.pageName = self.driver.find_element_by_id("com.ismartgo.apppub:id/tv_title").text
        except Exception as e:
            self.common_method.cutScreenShot (self.driver,"首页推荐 - 点击网购推荐")
            self.assertEqual(None, "执行失败，请查看截图")
        self.assertEqual(self.pageName,"规则说明")
        self.driver.find_element_by_id("com.ismartgo.apppub:id/tv_left").click()
        self.assertEqual(self.driver.current_activity, "com.ismartgo.app.activity.Tab_Container_Activity")

    def test_swipeRetail(self):
        u"测试首页 - 左右滑动零售商"
        try:
            self.common_method.adpass(self.driver)
            self.common_method.pop_ads(self.driver)
            #上滑屏幕到我的关注模块
            self.common_method.swipe_up(self.driver,t=500,n=4)
            y =self.driver.find_element_by_id("com.ismartgo.apppub:id/imgv_new_msg").size["height"]
            x = self.driver.get_window_size()["width"]
            #左滑、右滑
            self.driver.swipe(x*0.75,y*2,x*0.25,y*2,500)
            self.driver.swipe(x*0.25,y*2,x*0.75,y*2,500)
            time.sleep(1)
        except :
            self.common_method.cutScreenShot (self.driver,"左右滑动零售商")
            self.assertEqual(None, "执行失败，请查看截图")

    def test_clickRetail(self):
        u"测试首页 - 点击零售商按钮"
        try:
            self.common_method.adpass(self.driver)
            self.common_method.pop_ads(self.driver)
            #上滑屏幕到我的关注模块
            self.common_method.swipe_up(self.driver,t=500,n=1)
            #点击不同的零售商按钮
            self.driver.find_elements_by_id("com.ismartgo.apppub:id/cb_tab")[1].click()
            time.sleep(2)
            self.driver.find_elements_by_id("com.ismartgo.apppub:id/cb_tab")[2].click()
            time.sleep(2)
            self.driver.find_elements_by_id ("com.ismartgo.apppub:id/cb_tab")[0].click()
            time.sleep(2)
        except :
            self.common_method.cutScreenShot(self.driver,"点击首页零售商按钮")
            self.assertEqual(None,"执行失败，请查看截图")