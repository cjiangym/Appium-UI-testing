#coding:utf-8

from appium import webdriver
import unittest
import time
from common.common_method import Common_method

class PromotionTest(unittest.TestCase):
    common_method = Common_method ()

    def setUp(self):
        self.driver = Common_method.setUp(self)
        time.sleep(5)
    def tearDown(self):
        self.driver.quit()

    def test_shopHomePage_01(self):
        u"测试从首页跳转到商店主页"
        result = False
        try:
            self.common_method.init_case()                       #判断开屏广告
            self.common_method.pop_ads()                         #关闭弹窗广告
            x1 = self.driver.find_element_by_class_name("android.widget.ImageView").location["x"]
            y1 = self.driver.find_element_by_class_name("android.widget.ImageView").location["y"]
            x2 = self.driver.find_element_by_id ("com.ismartgo.apppub:id/ll_tab1").location["x"]
            y2 = self.driver.find_element_by_id ("com.ismartgo.apppub:id/ll_tab1").location["y"]
            self.driver.swipe(x1,y2,x2,y1,duration=None)
            shopLogo_list = self.driver.find_elements_by_id("com.ismartgo.apppub:id/shopLogo")
            shopLogo_list[0].click()
        except Exception as e:
            self.common_method.cutScreenShot ("test_ClickShopSign" + "_" + self.common_method.timestamp)
            self.assertEqual (result, "执行失败，请查看截图")
        time.sleep(3)
        activity = self.driver.current_activity
        self.assertEqual(activity,"com.ismartgo.app.activity.StoreHomeActivity")
        self.driver.find_element_by_id ("com.ismartgo.apppub:id/iv_left").click ()
        self.assertEqual(self.driver.current_activity,"com.ismartgo.app.activity.Tab_Container_Activity")


    def test_shopHomePage_02(self):
        u"测试从促销优惠列表点击商店logo进入商店主页"
        result = False
        try:
            self.common_method.init_case()                       #判断开屏广告
            self.common_method.pop_ads()                         #关闭弹窗广告
            tab_list = self.driver.find_elements_by_id("com.ismartgo.apppub:id/tab_Item_layout")
            tab_list[1].click()               #点击促销优惠tab
            time.sleep(3)
            shopLogo_list = self.driver.find_elements_by_id("com.ismartgo.apppub:id/store_logo")
            shopLogo_list[1].click()         #点击第二家门店上的logo
        except Exception as e:
            self.common_method.cutScreenShot ("test_ClickShopSign" + "_" + self.common_method.timestamp)
            self.assertEqual (result, "执行失败，请查看截图")
        time.sleep (3)
        activity = self.driver.current_activity
        self.assertEqual (activity, "com.ismartgo.app.activity.StoreHomeActivity")



    def test_shopHomePage_03(self):
        u"测试从促销优惠列表点击商品图片进入商店主页"
        result = False
        try:
            self.common_method.init_case()                       #判断开屏广告
            self.common_method.pop_ads()                         #关闭弹窗广告
            tab_list = self.driver.find_elements_by_id ("com.ismartgo.apppub:id/tab_Item_layout")
            tab_list[1].click ()  # 点击促销优惠tab
            time.sleep (3)
            pic_list = self.driver.find_elements_by_id("com.ismartgo.apppub:id/store_product_pic_1")
            pic_list[1].click()
        except Exception as e:
            self.common_method.cutScreenShot ("test_ClickShopSign" + "_" + self.common_method.timestamp)
            self.assertEqual (result, "执行失败，请查看截图")
        time.sleep (3)
        activity = self.driver.current_activity
        self.assertEqual (activity, "com.ismartgo.app.activity.StoreHomeActivity")


    def test_shopHomePage_04(self):
        u"测试从促销优惠列表点击“去看看”进入商店主页"
        result = False
        try:
            self.common_method.init_case ()  # 判断开屏广告
            self.common_method.pop_ads ()  # 关闭弹窗广告
            tab_list = self.driver.find_elements_by_id ("com.ismartgo.apppub:id/tab_Item_layout")
            tab_list[1].click ()  # 点击促销优惠tab
            time.sleep (3)
            scan_list = self.driver.find_elements_by_id ("com.ismartgo.apppub:id/scan_more")
            scan_list[1].click()
        except Exception as e:
            self.common_method.cutScreenShot ("test_ClickShopSign" + "_" + self.common_method.timestamp)
            self.assertEqual (result, "执行失败，请查看截图")
        time.sleep (3)
        self.assertEqual (self.driver.current_activity,"com.ismartgo.app.activity.StoreHomeActivity")
        self.driver.find_element_by_id("com.ismartgo.apppub:id/iv_left").click()
        self.assertEqual(self.driver.current_activity,"com.ismartgo.app.activity.Tab_Container_Activity")






