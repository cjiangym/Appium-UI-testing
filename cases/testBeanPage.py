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

    def test_offLineBean(self):
        u"测试线下赚豆板块"
        try:
            Common_method.adpass(self,self.driver)
            Common_method.pop_ads(self,self.driver)
            '''点击精明豆tab'''
            self.driver.find_elements_by_id ("com.ismartgo.apppub:id/tab_Item_layout")[3].click ()
            self.driver.implicitly_wait(5)
            try:
                Common_method.swipe_up(self,self.driver,t=500,n=1)
            except:
                Common_method.swipe_up (self, self.driver, t=500, n=1)
            '''检查是否有线下赚豆板块'''
            loc_text = 'new UiSelector().text("线下赚豆")'
            self.driver.find_element_by_android_uiautomator(loc_text)
            '''点击各个板块'''
            time.sleep(2)
            loc_text_sign = 'new UiSelector().text("到店签到")'
            self.driver.find_element_by_android_uiautomator(loc_text_sign).click()
            self.assertEqual(self.driver.find_element_by_id("com.ismartgo.apppub:id/tv_title").text,"到店签到")
            self.driver.find_element_by_id("com.ismartgo.apppub:id/pv_back").click()
            self.assertEqual(self.driver.current_activity,"com.ismartgo.app.activity.Tab_Container_Activity")
            loc_text_scan = 'new UiSelector().text("扫描商品")'
            self.driver.find_element_by_android_uiautomator(loc_text_scan).click()
            self.assertEqual(self.driver.find_element_by_id("com.ismartgo.apppub:id/tv_title").text,"商品扫描")
            self.driver.find_element_by_id ("com.ismartgo.apppub:id/tv_left").click()
            self.assertEqual(self.driver.current_activity,"com.ismartgo.app.activity.Tab_Container_Activity")
            loc_text_receipt = 'new UiSelector().text("拍立赚")'
            self.driver.find_element_by_android_uiautomator(loc_text_receipt).click()
            self.assertEqual(self.driver.find_element_by_id("com.ismartgo.apppub:id/rb_all").text,"全部")
            self.driver.find_element_by_id ("com.ismartgo.apppub:id/tv_left").click()
            self.assertEqual(self.driver.current_activity,"com.ismartgo.app.activity.Tab_Container_Activity")
        except:
            Common_method.cutScreenShot (self, self.driver, "精明豆-线下赚豆板块")
            self.assertTrue (None, "执行失败，请查看截图")

    def test_onLineBean(self):
        u"测试网购赚豆板块"
        try:
            Common_method.adpass(self,self.driver)
            Common_method.pop_ads(self,self.driver)
            '''点击精明豆tab'''
            self.driver.find_elements_by_id ("com.ismartgo.apppub:id/tab_Item_layout")[3].click ()
            self.driver.implicitly_wait(5)
            try:
                Common_method.swipe_up(self,self.driver,t=500,n=2)
            except:
                Common_method.swipe_up (self, self.driver, t=500, n=2)
            '''检查是否有网购赚豆板块'''
            loc_text = 'new UiSelector().text("网购赚")'
            self.driver.find_element_by_android_uiautomator(loc_text)
            '''点击各个板块'''
            time.sleep(2)
            loc_text_shop = 'new UiSelector().text("商城赚")'
            self.driver.find_element_by_android_uiautomator(loc_text_shop).click()
            self.assertEqual(self.driver.find_element_by_id("com.ismartgo.apppub:id/tv_title").text,"商城赚")
            self.driver.find_element_by_id("com.ismartgo.apppub:id/tv_left").click()
            self.assertEqual(self.driver.current_activity,"com.ismartgo.app.activity.Tab_Container_Activity")
            loc_text_goods = 'new UiSelector().text("超级赚")'
            self.driver.find_element_by_android_uiautomator(loc_text_goods).click()
            self.assertEqual(self.driver.find_element_by_id("com.ismartgo.apppub:id/tv_title").text,"超级赚")
            self.driver.find_element_by_id ("com.ismartgo.apppub:id/tv_left").click()
            self.assertEqual(self.driver.current_activity,"com.ismartgo.app.activity.Tab_Container_Activity")
            loc_text_taobao = 'new UiSelector().text("淘宝赚")'
            self.driver.find_element_by_android_uiautomator(loc_text_taobao).click()
            self.assertEqual(self.driver.find_element_by_id("com.ismartgo.apppub:id/tv_title").text,"淘宝赚")
            self.driver.find_element_by_id ("com.ismartgo.apppub:id/tv_left").click()
            self.assertEqual(self.driver.current_activity,"com.ismartgo.app.activity.Tab_Container_Activity")
        except:
            Common_method.cutScreenShot (self, self.driver, "精明豆-网购赚豆板块")
            self.assertTrue (None, "执行失败，请查看截图")

    def test_taskBean(self):
        u"测试任务赚豆板块"
        try:
            Common_method.adpass(self,self.driver)
            Common_method.pop_ads(self,self.driver)
            '''点击精明豆tab'''
            self.driver.find_elements_by_id ("com.ismartgo.apppub:id/tab_Item_layout")[3].click ()
            self.driver.implicitly_wait(5)
            try:
                Common_method.swipe_up(self,self.driver,t=500,n=4)
            except:
                Common_method.swipe_up (self, self.driver, t=500, n=4)
            '''检查是否有任务赚豆板块'''
            loc_text = 'new UiSelector().text("任务赚豆")'
            self.driver.find_element_by_android_uiautomator(loc_text)
            '''点击各个板块'''
            time.sleep(2)
            loc_text_invite = 'new UiSelector().text("邀请有礼")'
            self.driver.find_element_by_android_uiautomator(loc_text_invite).click()
            self.assertEqual(self.driver.find_element_by_id("com.ismartgo.apppub:id/tv_title").text,"邀请好友")
            self.driver.find_element_by_id("com.ismartgo.apppub:id/tv_left").click()
            self.assertEqual(self.driver.current_activity,"com.ismartgo.app.activity.Tab_Container_Activity")
            loc_text_sign = 'new UiSelector().text("每日签到")'
            self.driver.find_element_by_android_uiautomator(loc_text_sign).click()
            self.assertEqual(self.driver.find_element_by_id("com.ismartgo.apppub:id/tv_title").text,"每日签到")
            self.driver.find_element_by_id ("com.ismartgo.apppub:id/tv_left").click()
            self.assertEqual(self.driver.current_activity,"com.ismartgo.app.activity.Tab_Container_Activity")
            loc_text_accout = 'new UiSelector().text("记账达人圈")'
            self.driver.find_element_by_android_uiautomator(loc_text_accout).click()
            self.assertEqual(self.driver.find_element_by_id("com.ismartgo.apppub:id/tv_title").text,"详情")
            self.driver.find_element_by_id ("com.ismartgo.apppub:id/tv_left").click()
            self.assertEqual(self.driver.current_activity,"com.ismartgo.app.activity.Tab_Container_Activity")
        except:
            Common_method.cutScreenShot (self, self.driver, "精明豆-任务赚豆板块")
            self.assertTrue (None, "执行失败，请查看截图")

    def test_gameBean(self):
        u"测试精明豆-游戏中心板块"
        try:
            Common_method.adpass(self,self.driver)
            Common_method.pop_ads(self,self.driver)
            '''点击精明豆tab'''
            self.driver.find_elements_by_id ("com.ismartgo.apppub:id/tab_Item_layout")[3].click ()
            self.driver.implicitly_wait(5)
            try:
                Common_method.swipe_up(self,self.driver,t=500,n=5)
            except:
                Common_method.swipe_up (self, self.driver, t=500, n=5)
            '''检查是否有任务赚豆板块'''
            loc_text = 'new UiSelector().text("游戏中心")'
            self.driver.find_element_by_android_uiautomator(loc_text)
            '''点击各个板块'''
            time.sleep(2)
            loc_text_game = 'new UiSelector().text("疯狂老虎机")'
            self.driver.find_element_by_android_uiautomator(loc_text_game).click()
            self.assertEqual(self.driver.find_element_by_id("com.ismartgo.apppub:id/tv_title").text,"详情")
            self.driver.find_element_by_id("com.ismartgo.apppub:id/tv_left").click()
            self.assertEqual(self.driver.current_activity,"com.ismartgo.app.activity.Tab_Container_Activity")
            loc_text_more= 'new UiSelector().text("敬请期待")'
            self.driver.find_element_by_android_uiautomator(loc_text_more)
            time.sleep(2)
        except:
            Common_method.cutScreenShot (self, self.driver, "精明豆-游戏中心板块")
            self.assertTrue (None, "执行失败，请查看截图")


