#coding:utf-8
from appium import webdriver
import unittest
import time
from common.common_method import Common_method

class PromotionTest(unittest.TestCase):
    common_method = Common_method()

    def setUp(self):
        self.driver = self.common_method.setUp()
        time.sleep(3)
    def tearDown(self):
        self.driver.quit()

    def test_shopHomePage_01(self):
        u"测试从首页跳转到商店主页"
        result = False
        try:
            #self.common_method.init_case()                       #判断开屏广告
            self.common_method.pop_ads()                         #关闭弹窗广告
            x1 = self.driver.find_element_by_class_name("android.widget.ImageView").location["x"]
            y1 = self.driver.find_element_by_class_name("android.widget.ImageView").location["y"]
            x2 = self.driver.find_element_by_id ("com.ismartgo.apppub:id/ll_tab1").location["x"]
            y2 = self.driver.find_element_by_id ("com.ismartgo.apppub:id/ll_tab1").location["y"]
            self.driver.swipe(x1,y2,x2,y1,duration=None)
            shopLogo_list = self.driver.find_elements_by_id("com.ismartgo.apppub:id/shopLogo")
            shopLogo_list[0].click()
        except Exception as e:
            self.common_method.cutScreenShot ("test_shopHomePage_01" + "_" + self.common_method.timestamp)
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
            self.common_method.cutScreenShot ("test_shopHomePage_02" + "_" + self.common_method.timestamp)
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
            self.common_method.cutScreenShot ("test_shopHomePage_03" + "_" + self.common_method.timestamp)
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
            self.common_method.cutScreenShot ("test_shopHomePage_04" + "_" + self.common_method.timestamp)
            self.assertEqual (result, "执行失败，请查看截图")
        time.sleep (3)
        self.assertEqual (self.driver.current_activity,"com.ismartgo.app.activity.StoreHomeActivity")
        self.driver.find_element_by_id("com.ismartgo.apppub:id/iv_left").click()
        self.assertEqual(self.driver.current_activity,"com.ismartgo.app.activity.Tab_Container_Activity")

    def test_selectDistrict_01(self):
        u"测试促销优惠选择区域-附近（智能范围）"
        result = False
        try:
            self.common_method.init_case ()  # 判断开屏广告
            self.common_method.pop_ads ()  # 关闭弹窗广告
            tab_list = self.driver.find_elements_by_id ("com.ismartgo.apppub:id/tab_Item_layout")
            tab_list[1].click ()  # 点击促销优惠tab
            time.sleep (3)
            self.driver.find_element_by_id("com.ismartgo.apppub:id/tv_district").click()     #点击右上角“附近”选择
            loc_text = 'new UiSelector().text("附近（智能范围）")'
            self.driver.find_element_by_android_uiautomator(loc_text).click()                      #选择附近（智能范围）
            time.sleep (3)
            self.text = self.driver.find_element_by_id ("com.ismartgo.apppub:id/tv_district").text
        except Exception as e:
            self.common_method.cutScreenShot ("test_selectDistrict_01" + "_" + self.common_method.timestamp)
            self.assertEqual (result, "执行失败，请查看截图")
        self.assertEqual (self.text, "附近")                    #检查选择之后促销优惠右上角文字显示

    def test_selectDistrict_02(self):
        u"测试促销优惠选择区域-附近1000米"
        result = False
        try:
            self.common_method.init_case ()  # 判断开屏广告
            self.common_method.pop_ads ()  # 关闭弹窗广告
            tab_list = self.driver.find_elements_by_id ("com.ismartgo.apppub:id/tab_Item_layout")
            tab_list[1].click ()  # 点击促销优惠tab
            time.sleep (3)
            self.driver.find_element_by_id("com.ismartgo.apppub:id/tv_district").click()    #点击右上角“附近”选择
            loc_text = 'new UiSelector().text("1000米")'
            self.driver.find_element_by_android_uiautomator(loc_text).click()                  #选择附近1000米
            time.sleep (3)
            self.text = self.driver.find_element_by_id ("com.ismartgo.apppub:id/tv_district").text
        except Exception as e:
            self.common_method.cutScreenShot ("test_selectDistrict_02" + "_" + self.common_method.timestamp)
            self.assertEqual (result, "执行失败，请查看截图")
        self.assertEqual(self.text, "1000...")                       #检查选择之后促销优惠右上角文字显示

    def test_selectDistrict_03(self):
        u"测试促销优惠选择区域-全部商区"
        result = False
        try:
            self.common_method.init_case ()  # 判断开屏广告
            self.common_method.pop_ads ()  # 关闭弹窗广告
            tab_list = self.driver.find_elements_by_id ("com.ismartgo.apppub:id/tab_Item_layout")
            tab_list[1].click ()  # 点击促销优惠tab
            time.sleep (3)
            self.driver.find_element_by_id("com.ismartgo.apppub:id/tv_district").click()            #点击右上角“附近”选择
            district_list = self.driver.find_elements_by_id("com.ismartgo.apppub:id/popup_menu_name")
            district_list[1].click()
            loc_text = 'new UiSelector().text("全部")'
            self.driver.find_element_by_android_uiautomator(loc_text).click()            #选择全部商区-全部
            time.sleep (3)
            self.text = self.driver.find_element_by_id ("com.ismartgo.apppub:id/tv_district").text
        except Exception as e:
            self.common_method.cutScreenShot ("test_selectDistrict_03" + "_" + self.common_method.timestamp)
            self.assertEqual (result, "执行失败，请查看截图")
        self.assertEqual (self.text, "全部商区")                                 #检查选择之后促销优惠右上角文字显示

    def test_selectDistrict_04(self):
        u"测试促销优惠选择区域-选择某个区域"
        result = False
        try:
            self.common_method.init_case ()  # 判断开屏广告
            self.common_method.pop_ads ()  # 关闭弹窗广告
            tab_list = self.driver.find_elements_by_id ("com.ismartgo.apppub:id/tab_Item_layout")
            tab_list[1].click ()  # 点击促销优惠tab
            time.sleep (3)
            self.driver.find_element_by_id("com.ismartgo.apppub:id/tv_district").click()        #点击右上角“附近”选择
            self.district_list = self.driver.find_elements_by_id("com.ismartgo.apppub:id/popup_menu_name")
            self.district_list[2].click()                     #选择区域
            self.text_selected = self.district_list[2].text        #用于后面断言结果
            loc_text = 'new UiSelector().text("全部")'
            self.driver.find_element_by_android_uiautomator(loc_text).click()                   #点击区域下的全部商圈
            time.sleep (3)
            self.text = self.driver.find_element_by_id ("com.ismartgo.apppub:id/tv_district").text
        except Exception as e:
            self.common_method.cutScreenShot ("test_selectDistrict_04" + "_" + self.common_method.timestamp)
            self.assertEqual (result, "执行失败，请查看截图")
        self.assertEqual (self.text, self.text_selected)

    def test_selectShoptype_01(self):
        u"测试选择商店类型"
        result = False
        try:
            self.common_method.init_case ()  # 判断开屏广告
            self.common_method.pop_ads ()  # 关闭弹窗广告
            tab_list = self.driver.find_elements_by_id ("com.ismartgo.apppub:id/tab_Item_layout")
            tab_list[1].click ()  # 点击促销优惠tab
            time.sleep (3)
            shoptype_list = self.driver.find_elements_by_class_name("android.widget.Button")
            shoptype_list[0].click()
        except Exception as e:
            self.common_method.cutScreenShot ("test_selectShoptype_01" + "_" + self.common_method.timestamp)
            self.assertEqual (result, "执行失败，请查看截图")
    def test_selectShoptype_02(self):
        u"测试选择商店类型"
        result = False
        try:
            self.common_method.init_case ()  # 判断开屏广告
            self.common_method.pop_ads ()  # 关闭弹窗广告
            tab_list = self.driver.find_elements_by_id ("com.ismartgo.apppub:id/tab_Item_layout")
            tab_list[1].click ()  # 点击促销优惠tab
            time.sleep (3)
            shoptype_list = self.driver.find_elements_by_class_name("android.widget.Button")
            shoptype_list[1].click()
        except Exception as e:
            self.common_method.cutScreenShot ("test_selectShoptype_02" + "_" + self.common_method.timestamp)
            self.assertEqual (result, "执行失败，请查看截图")

    def test_selectShoptype_03(self):
        u"测试左右滑动商店类型"
        result = False
        try:
            self.common_method.init_case ()  # 判断开屏广告
            self.common_method.pop_ads ()  # 关闭弹窗广告
            tab_list = self.driver.find_elements_by_id ("com.ismartgo.apppub:id/tab_Item_layout")
            tab_list[1].click ()  # 点击促销优惠tab
            time.sleep (3)
            #左滑商店类型区域
            x0=0
            x1 = self.driver.get_window_size()["width"]
            y = self.driver.find_element_by_id("com.ismartgo.apppub:id/base_layout").size["height"]
            y1 = y+y*2/3
            if isinstance(y1,float):
                y1 = int(y1)
            self.driver.swipe(x1*0.75,y1,x0,y1,duration=1000)
            self.driver.swipe(x0, y1, x1*0.75, y1, duration=1000)
        except:
            self.common_method.cutScreenShot ("test_selectShoptype_03" + "_" + self.common_method.timestamp)
            self.assertEqual (result, "执行失败，请查看截图")








