#coding utf-8
from appium import webdriver
import unittest
import time
from common.common_method import Common_method

#-------------购物清单功能测试--------------
class MycollectTest(unittest.TestCase):
    common_method = Common_method()
    def setUp(self):
        self.driver = self.common_method.setUp()
        time.sleep(3)
    def tearDown(self):
        self.driver.quit()

    def test_mycollectList(self):
        u"测试我的购物清单列表"
        try:
            self.common_method.adpass(self.driver)
            self.common_method.pop_ads(self.driver)
            '''点击购物清单tab'''
            self.driver.find_elements_by_id("com.ismartgo.apppub:id/tab_Item_layout")[2].click()
            time.sleep(1)
            pageName = self.driver.find_element_by_id("com.ismartgo.apppub:id/tv_title").text
            self.assertEqual(pageName,"购物清单")
            '''没有收藏过，则点击收藏按钮跳转到促销优惠列表'''
            self.driver.find_element_by_id("com.ismartgo.apppub:id/ll_base_empty")
        except:
            '''有收藏过，则点击第一个取消收藏'''
            self.driver.find_element_by_id ("com.ismartgo.apppub:id/iv_shopping_list_collect").click ()
            time.sleep(1)
        else:
            try:
                self.driver.find_element_by_id("com.ismartgo.apppub:id/btn_base_empty").click()
                self.driver.implicitly_wait(8)
                self.driver.find_element_by_id("com.ismartgo.apppub:id/scan_more").click()
                self.driver.implicitly_wait(8)
                self.driver.find_element_by_id("com.ismartgo.apppub:id/mer_collect").click()
                time.sleep(2)
                self.driver.find_element_by_id("com.ismartgo.apppub:id/tv_left").click()
            except:
                self.common_method.cutScreenShot (self.driver,"购物清单列表")
                self.assertEqual(None,"执行失败，请查看截图")

    def test_collectInvalidList_01(self):
        u"测试我的购物清单列表-失效购物清单,取消清空购物清单"
        try:
            self.common_method.adpass(self.driver)
            self.common_method.pop_ads(self.driver)
            '''点击购物清单tab'''
            tab_list = self.driver.find_elements_by_id("com.ismartgo.apppub:id/tab_Item_layout")
            tab_list[2].click()
            #在购物清单页面点击已失效按钮
            time.sleep(1)
            self.driver.find_element_by_id("com.ismartgo.apppub:id/tv_right").click()
            time.sleep(1)
            invalidButton = self.driver.find_element_by_id("com.ismartgo.apppub:id/tv_right")
            if invalidButton.is_enabled():
                invalidButton.click()
                self.driver.find_element_by_id("com.ismartgo.apppub:id/tv_alert_cancel").click()
                self.assertEqual(self.driver.current_activity,"com.ismartgo.app.activity.ShoppingListExpiredActivity")
            else:
                self.driver.find_element_by_id("com.ismartgo.apppub:id/tv_left").click()
                self.assertEqual (self.driver.current_activity, "com.ismartgo.app.activity.Tab_Container_Activity")
        except:
            self.common_method.cutScreenShot (self.driver,"取消一键清空购物清单")
            self.assertEqual(None, "执行失败，请查看截图")

    def test_collectInvalidList_02(self):
        u"测试我的购物清单列表-失效购物清单,清空购物清单"
        try:
            self.common_method.adpass(self.driver)
            self.common_method.pop_ads(self.driver)
            '''点击购物清单tab'''
            tab_list = self.driver.find_elements_by_id("com.ismartgo.apppub:id/tab_Item_layout")
            tab_list[2].click()
            #在购物清单页面点击已失效按钮
            time.sleep(1)
            self.driver.find_element_by_id("com.ismartgo.apppub:id/tv_right").click()
            time.sleep(1)
            invalidButton = self.driver.find_element_by_id("com.ismartgo.apppub:id/tv_right")
            if invalidButton.is_enabled():
                invalidButton.click()
                self.driver.find_element_by_id("com.ismartgo.apppub:id/tv_alert_ensure").click()
                self.assertEqual(self.driver.current_activity,"com.ismartgo.app.activity.ShoppingListExpiredActivity")
            else:
                self.driver.find_element_by_id("com.ismartgo.apppub:id/tv_left").click()
                self.assertEqual (self.driver.current_activity, "com.ismartgo.app.activity.Tab_Container_Activity")
        except:
            self.common_method.cutScreenShot (self.driver,"一键清空购物清单")
            self.assertEqual(None, "执行失败，请查看截图")





