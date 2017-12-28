#coding:utf-8

from appium import webdriver
import unittest
import time
from common.common_method import Common_method

class MyBeanTest(unittest.TestCase):

    def setUp(self):
        self.driver = Common_method.setUp(self)
        time.sleep(3)
    def tearDown(self):
        self.driver.quit()

    def test_myBean(self):
        u"查看我的精明豆"
        try:
            Common_method.adpass(self,self.driver)
            Common_method.pop_ads(self,self.driver)
            '''点击精明豆tab'''
            self.driver.find_elements_by_id("com.ismartgo.apppub:id/tab_Item_layout")[3].click()
            self.driver.implicitly_wait(5)
            '''点击精明豆数量区域'''
            self.driver.find_element_by_id("com.ismartgo.apppub:id/tv_bean_count").click()
            time.sleep(2)
            pageName = self.driver.find_element_by_id("com.ismartgo.apppub:id/tv_title").text
            self.assertEqual(pageName,"明细")
            '''点击赚按钮'''
            self.driver.find_element_by_id("com.ismartgo.apppub:id/tv_earn").click()
            self.driver.implicitly_wait(5)
            '''查看是否有记录存在'''
            self.driver.find_element_by_id ("com.ismartgo.apppub:id/tv_num")
            '''点击花按钮'''
            self.driver.find_element_by_id("com.ismartgo.apppub:id/tv_cost").click()
            time.sleep(1)
            self.driver.find_element_by_id ("com.ismartgo.apppub:id/tv_left").click ()
            time.sleep(1)
            self.assertEqual (self.driver.current_activity, "com.ismartgo.app.activity.Tab_Container_Activity")
        except:
            Common_method.cutScreenShot(self,self.driver,"查看精明豆")
            self.assertTrue(None,"执行失败，请查看截图")

    def test_myGrade(self):
        u"点击等级图标"
        try:
            Common_method.adpass(self,self.driver)
            Common_method.pop_ads(self,self.driver)
            '''点击精明豆tab'''
            self.driver.find_elements_by_id ("com.ismartgo.apppub:id/tab_Item_layout")[3].click ()
            self.driver.implicitly_wait(5)
            self.driver.find_element_by_id("com.ismartgo.apppub:id/img_member_grade").click()
            self.driver.implicitly_wait(5)
            pageName = self.driver.find_element_by_id("com.ismartgo.apppub:id/tv_title").text
            pageName_2 = self.driver.find_element_by_id("com.ismartgo.apppub:id/tv_right").text
            self.assertEqual(pageName,"详情")
            self.assertEqual(pageName_2,"积分明细")
            self.driver.find_element_by_id("com.ismartgo.apppub:id/tv_left").click()
            time.sleep(1)
            self.assertEqual(self.driver.current_activity,"com.ismartgo.app.activity.Tab_Container_Activity")
        except:
            Common_method.cutScreenShot(self,self.driver,"点击等级图标")
            self.assertTrue(None,"执行失败，请查看截图")
