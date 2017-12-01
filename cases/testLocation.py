#coding utf-8
from appium import webdriver
import unittest
import time
from common.common_method import Common_method

class LocationTest(unittest.TestCase):
    common_method = Common_method()

    def setUp(self):
        self.driver = self.common_method.setUp()
        self.driver.wait_activity ("com.ismartgo.app.activity.Tab_Container_Activity", 10)
    def tearDown(self):
        self.driver.quit()

    def test_location_01(self):
        u"测试城市定位,检查自动定位功能"
        result = False
        try:
            self.common_method.adpass(self.driver)
            self.common_method.pop_ads(self.driver)
            self.driver.find_element_by_id("com.ismartgo.apppub:id/layout_select_city").click()
            time.sleep(2)
            self.pageName = self.driver.find_element_by_id("com.ismartgo.apppub:id/tv_title").text
            self.locationName = self.driver.find_element_by_id("com.ismartgo.apppub:id/btn_locationcity").text
        except Exception as e:
            self.common_method.cutScreenShot("test_location_01"+"_"+self.common_method.timestamp)
            self.assertEqual(result,"执行失败，请查看截图")
        self.assertEqual(self.pageName,"选择位置")
        self.assertNotEqual(self.locationName,"重新定位")

    def test_location_02(self):
        u"测试城市定位，选择城市"
        result = False
        try:
            self.common_method.adpass(self.driver)
            self.common_method.pop_ads(self.driver)
            self.driver.find_element_by_id("com.ismartgo.apppub:id/layout_select_city").click()
            time.sleep(2)
            city_list = self.driver.find_elements_by_class_name("android.view.View")
            city_list[1].click()             #点击城市列表上的第一个城市名：阿坝
            time.sleep(1)
            self.locationName = self.driver.find_element_by_id("com.ismartgo.apppub:id/tv_new_location").text
        except Exception as e:
            self.common_method.cutScreenShot("test_location_02"+"_"+self.common_method.timestamp)
            self.assertEqual(result,"执行失败，请查看截图")
        self.assertEqual(self.locationName,"阿坝")

    def test_location_03(self):
        u"测试城市定位，检查最近访问的城市"
        result = False
        try:
            self.common_method.adpass(self.driver)
            self.common_method.pop_ads(self.driver)
            self.driver.find_element_by_id("com.ismartgo.apppub:id/layout_select_city").click()
            time.sleep(2)
            city_list = self.driver.find_elements_by_class_name("android.widget.Button")
            self.locationName = city_list[1].text             #最近访问城市城市名：阿坝
        except Exception as e:
            self.common_method.cutScreenShot("test_location_02"+"_"+self.common_method.timestamp)
            self.assertEqual(result,"执行失败，请查看截图")
        self.assertEqual(self.locationName,"阿坝")

    def test_location_04(self):
        u"测试城市定位，搜索城市后选择城市"
        result = False
        try:
            self.common_method.adpass(self.driver)
            self.common_method.pop_ads(self.driver)
            self.driver.find_element_by_id("com.ismartgo.apppub:id/layout_select_city").click()
            time.sleep(2)
            '''点击搜索框'''
            self.driver.find_element_by_id("com.ismartgo.apppub:id/layout_search_city").click()
            '''输入厦门'''
            self.driver.find_element_by_id("com.ismartgo.apppub:id/et_search").send_keys("厦门")
            '''选择搜索结果列表中的厦门'''
            self.driver.find_element_by_id("com.ismartgo.apppub:id/history_tag").click()
            self.locationName = self.driver.find_element_by_id ("com.ismartgo.apppub:id/tv_new_location").text
        except Exception as e:
            self.common_method.cutScreenShot("test_location_02"+"_"+self.common_method.timestamp)
            self.assertEqual(result,"执行失败，请查看截图")
        self.assertEqual(self.locationName,"厦门")


