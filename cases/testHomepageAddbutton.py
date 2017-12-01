from appium import webdriver
import unittest
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from common.common_method import Common_method

class H5Test(unittest.TestCase):
    common_method = Common_method()
    def setUp(self):
        self.driver = self.common_method.setUp()
        self.driver.wait_activity ("com.ismartgo.app.activity.Tab_Container_Activity", 10)
    def tearDown(self):
        self.driver.quit()

    def test_dailySign(self):
        u"测试跳转到每日签到h5"
        result = False
        try:
            self.common_method.adpass(self.driver)
            self.common_method.pop_ads(self.driver)
            self.driver.find_element_by_id("com.ismartgo.apppub:id/img_msg").click()
            '''
            x1 = self.driver.find_element_by_id("com.ismartgo.apppub:id/layout_select_city").size["width"]
            x = self.driver.find_element_by_id("com.ismartgo.apppub:id/layout_new_search").size["width"]
            y1 = self.driver.find_element_by_id("com.ismartgo.apppub:id/imgv_new_msg").size["height"]
            y = self.driver.find_element_by_id("com.ismartgo.apppub:id/rl_top_group").size["height"]
            self.driver.tap([(x1+x,y1+y)],duration=None)                        #计算出屏幕点击区域
            '''
            self.driver.find_element_by_id("com.ismartgo.apppub:id/ll_sign").click()
            self.driver.implicitly_wait(10)
            self.pageName = self.driver.find_element_by_id("com.ismartgo.apppub:id/tv_title").text
        except:
            self.common_method.cutScreenShot ( "test_dailySign" + "_" + self.common_method.timestamp)  # 异常后截图放在erroScreenShot文件夹下
            self.assertEqual (result, "执行失败，请查看截图")
        self.assertEqual(self.pageName,"每日签到")
        self.driver.find_element_by_id("com.ismartgo.apppub:id/tv_left").click()
        self.assertEqual (self.driver.current_activity,"com.ismartgo.app.activity.Tab_Container_Activity")

    def test_Msg_01(self):
        u"测试消息-点击进入消息中心"
        result = False
        try:
            self.common_method.adpass(self.driver)
            self.common_method.pop_ads(self.driver)
            '''点击+号按钮'''
            self.driver.find_element_by_id("com.ismartgo.apppub:id/img_msg").click()
            '''点击消息'''
            self.driver.find_element_by_id("com.ismartgo.apppub:id/ll_msg").click()
            self.driver.implicitly_wait(8)
            self.pageName = self.driver.find_element_by_id("com.ismartgo.apppub:id/tv_title").text
        except:
            self.common_method.cutScreenShot ( "test_Msg_01" + "_" + self.common_method.timestamp)  # 异常后截图放在erroScreenShot文件夹下
            self.assertEqual(result, "执行失败，请查看截图")
        self.assertEqual(self.pageName,"消息中心")
        self.driver.find_element_by_id("com.ismartgo.apppub:id/tv_left").click()
        self.assertEqual (self.driver.current_activity,"com.ismartgo.app.activity.Tab_Container_Activity")

    def test_Msg_02(self):
        u"测试消息-查看系统消息"
        result = False
        try:
            self.common_method.adpass(self.driver)
            self.common_method.pop_ads(self.driver)
            '''点击+号按钮'''
            self.driver.find_element_by_id("com.ismartgo.apppub:id/img_msg").click()
            '''点击消息'''
            self.driver.find_element_by_id("com.ismartgo.apppub:id/ll_msg").click()
            self.driver.implicitly_wait (8)
            '''点击系统消息'''
            self.driver.find_element_by_id("com.ismartgo.apppub:id/tv_msg_name").click()
            '''查看第一条消息'''
            msg_list = self.driver.find_elements_by_id("com.ismartgo.apppub:id/tv_txt_msg_details")
            msg_list[0].click()
            time.sleep(1)
            self.pageName = self.driver.find_element_by_id("com.ismartgo.apppub:id/tv_title").text
            time.sleep(1)
            self.driver.find_element_by_id ("com.ismartgo.apppub:id/tv_left").click ()
            time.sleep(1)
            self.driver.find_element_by_id ("com.ismartgo.apppub:id/tv_left").click ()
            time.sleep(1)
            self.driver.find_element_by_id ("com.ismartgo.apppub:id/tv_left").click ()
        except:
            self.common_method.cutScreenShot ( "test_Msg_02" + "_" + self.common_method.timestamp)  # 异常后截图放在erroScreenShot文件夹下
            self.assertEqual(result, "执行失败，请查看截图")
        self.assertEqual(self.pageName,"详情")
        self.assertEqual (self.driver.current_activity,"com.ismartgo.app.activity.Tab_Container_Activity")

    def test_Msg_03(self):
        u"测试消息-一键全读"
        result = False
        try:
            self.common_method.adpass(self.driver)
            self.common_method.pop_ads(self.driver)
            '''点击+号按钮'''
            self.driver.find_element_by_id("com.ismartgo.apppub:id/img_msg").click()
            '''点击消息'''
            self.driver.find_element_by_id("com.ismartgo.apppub:id/ll_msg").click()
            self.driver.implicitly_wait (8)
            self.driver.find_element_by_id ("com.ismartgo.apppub:id/div_new_msg_count")
            '''如果有未读消息，点击系统消息，没有则返回首页'''
            self.driver.find_element_by_id("com.ismartgo.apppub:id/tv_msg_name").click()
            time.sleep(1)
            '''点击一键全读'''
            self.driver.find_element_by_id("com.ismartgo.apppub:id/tv_right").click()
            time.sleep(1)
            '''返回消息中心'''
            self.driver.find_element_by_id("com.ismartgo.apppub:id/tv_left").click()
            self.driver.find_element_by_id("com.ismartgo.apppub:id/div_new_msg_count")
        except:
            '''没有找到未读消息，则返回'''
            self.driver.find_element_by_id("com.ismartgo.apppub:id/tv_left").click()
        else:
            self.common_method.cutScreenShot( "test_Msg_03" + "_" + self.common_method.timestamp)  # 异常后截图放在erroScreenShot文件夹下
            self.assertEqual(result, "执行失败，请查看截图")
        self.assertEqual (self.driver.current_activity,"com.ismartgo.app.activity.Tab_Container_Activity")

    def test_Msg_04(self):
        u"测试消息-社区消息"
        result = False
        try:
            self.common_method.adpass(self.driver)
            self.common_method.pop_ads(self.driver)
            '''点击+号按钮'''
            self.driver.find_element_by_id("com.ismartgo.apppub:id/img_msg").click()
            '''点击消息'''
            self.driver.find_element_by_id("com.ismartgo.apppub:id/ll_msg").click()
            self.driver.implicitly_wait(8)
            '''点击社区消息'''
            msg_list = self.driver.find_elements_by_id("com.ismartgo.apppub:id/tv_msg_name")
            msg_list[1].click()
            time.sleep(1)
            self.pageName = self.driver.find_element_by_id("com.ismartgo.apppub:id/tv_title").text
            time.sleep(1)
            self.driver.find_element_by_id ("com.ismartgo.apppub:id/tv_left").click()
            time.sleep(1)
        except:
            self.common_method.cutScreenShot ( "test_Msg_04社区消息" + "_" + self.common_method.timestamp)  # 异常后截图放在erroScreenShot文件夹下
            self.assertEqual(result, "执行失败，请查看截图")
        self.assertEqual(self.pageName,"社区消息")
        self.driver.find_element_by_id("com.ismartgo.apppub:id/tv_left").click()
        self.assertEqual (self.driver.current_activity,"com.ismartgo.app.activity.Tab_Container_Activity")

    def test_Msg_05(self):
        u"测试消息-点赞消息"
        result = False
        try:
            self.common_method.adpass(self.driver)
            self.common_method.pop_ads(self.driver)
            '''点击+号按钮'''
            self.driver.find_element_by_id("com.ismartgo.apppub:id/img_msg").click()
            '''点击消息'''
            self.driver.find_element_by_id("com.ismartgo.apppub:id/ll_msg").click()
            self.driver.implicitly_wait (8)
            '''点击点赞消息'''
            msg_list = self.driver.find_elements_by_id("com.ismartgo.apppub:id/tv_msg_name")
            msg_list[2].click()
            time.sleep(1)
            self.pageName = self.driver.find_element_by_id("com.ismartgo.apppub:id/tv_title").text
            time.sleep(1)
            self.driver.find_element_by_id ("com.ismartgo.apppub:id/tv_left").click()
            time.sleep(1)
        except:
            self.common_method.cutScreenShot ( "test_Msg_04社区消息" + "_" + self.common_method.timestamp)  # 异常后截图放在erroScreenShot文件夹下
            self.assertEqual(result, "执行失败，请查看截图")
        self.assertEqual(self.pageName,"点赞消息")
        self.driver.find_element_by_id("com.ismartgo.apppub:id/tv_left").click()
        self.assertEqual (self.driver.current_activity,"com.ismartgo.app.activity.Tab_Container_Activity")

    def test_vipCard(self):
        u"点击+按钮下的会员卡，跳转到我的卡券页面"
        result = False
        try:
            self.common_method.adpass(self.driver)
            self.common_method.pop_ads(self.driver)
            '''点击+号按钮'''
            self.driver.find_element_by_id ("com.ismartgo.apppub:id/img_msg").click ()
            '''会员卡'''
            self.driver.find_element_by_id ("com.ismartgo.apppub:id/ll_membership").click()
            self.driver.implicitly_wait(8)
            self.pageName = self.driver.find_element_by_id("com.ismartgo.apppub:id/tv_title").text
        except Exception as e:
            self.common_method.cutScreenShot ( "test_vipCard" + "_" + self.common_method.timestamp)  # 异常后截图放在erroScreenShot文件夹下
            self.assertEqual(result,"执行失败，请查看截图")
        self.assertEqual(self.pageName,"我的卡劵")
        self.driver.find_element_by_id("com.ismartgo.apppub:id/tv_left").click()
        self.assertEqual (self.driver.current_activity,"com.ismartgo.app.activity.Tab_Container_Activity")

    def test_shoppingCard(self):
        u"点击+按钮下的购物卡，跳转到我的购物卡"
        result = False
        try:
            self.common_method.adpass(self.driver)
            self.common_method.pop_ads(self.driver)
            '''点击+号按钮'''
            self.driver.find_element_by_id ("com.ismartgo.apppub:id/img_msg").click ()
            '''购物卡'''
            #self.driver.find_element_by_id ("com.ismartgo.apppub:id/ll_shopping").click()
            loc_text = 'new UiSelector().text("购物卡")'
            self.driver.find_element_by_android_uiautomator(loc_text).click()
            self.driver.implicitly_wait(8)
            self.pageName = self.driver.find_element_by_id("com.ismartgo.apppub:id/tv_title").text
        except Exception as e:
            self.common_method.cutScreenShot ( "test_shoppingCard" + "_" + self.common_method.timestamp)  # 异常后截图放在erroScreenShot文件夹下
            self.assertEqual(result,"执行失败，请查看截图")
        self.assertEqual(self.pageName,"购物卡")
        self.driver.find_element_by_id("com.ismartgo.apppub:id/tv_left").click()
        self.assertEqual (self.driver.current_activity,"com.ismartgo.app.activity.Tab_Container_Activity")





