#coding utf-8
from appium import webdriver
import unittest
import time
from common.common_method import Common_method

class MycollectTest(unittest.TestCase):
    common_method = Common_method()
    def setUp(self):
        self.driver = self.common_method.setUp()
        time.sleep(3)
    def tearDown(self):
        self.driver.quit()

    def test_collectList(self):
        u"测试我的购物清单列表"
        result = False
        try:
            self.common_method.adpass(self.driver)
            self.common_method.pop_ads(self.driver)
            '''点击购物清单tab'''
            tab_list = self.driver.find_elements_by_id("com.ismartgo.apppub:id/tab_Item_layout")
            tab_list[2].click()
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
                time.sleep(2)
                self.driver.find_element_by_id("com.ismartgo.apppub:id/base_layout")
            except:
                self.common_method.cutScreenShot ("test_collectList" + "_" + self.common_method.timestamp)
                self.assertEqual(result, "执行失败，请查看截图")





