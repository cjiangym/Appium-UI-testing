#coding:utf-8

from appium import webdriver
import unittest
import time
from common.common_method import Common_method

class ExchangeGiftTest(unittest.TestCase):

    def setUp(self):
        self.driver = Common_method.setUp(self)
        time.sleep(3)

    def tearDown(self):
        self.driver.quit()

    def test_randomGift(self):
        u"测试精明豆页面两个随机礼品"
        try:
            Common_method.adpass(self,self.driver)
            Common_method.pop_ads(self,self.driver)
            '''点击精明豆tab'''
            self.driver.find_elements_by_id("com.ismartgo.apppub:id/tab_Item_layout")[3].click()
            self.driver.implicitly_wait(8)
            '''点击第一张礼品图片'''
            self.driver.find_elements_by_id("com.ismartgo.apppub:id/iv_logo")[0].click()
            pageTitle = self.driver.find_element_by_id("com.ismartgo.apppub:id/tv_title").text
            self.assertEqual(pageTitle,"礼品详情")
            '''查看立即兑换按钮'''
            self.driver.find_element_by_id("com.ismartgo.apppub:id/btn_confirm")
            self.driver.find_element_by_id("com.ismartgo.apppub:id/tv_left").click()
            self.assertEqual (self.driver.current_activity, "com.ismartgo.app.activity.Tab_Container_Activity")
            '''点击第二张礼品图片'''
            self.driver.find_elements_by_id ("com.ismartgo.apppub:id/iv_logo")[1].click()
            pageTitle = self.driver.find_element_by_id ("com.ismartgo.apppub:id/tv_title").text
            self.assertEqual (pageTitle, "礼品详情")
            self.driver.find_element_by_id ("com.ismartgo.apppub:id/btn_confirm")
            self.driver.find_element_by_id ("com.ismartgo.apppub:id/tv_left").click()
        except:
            Common_method.cutScreenShot(self,self.driver,"随机礼品")
            self.assertTrue(None,"执行失败，请查看截图")

    def test_giftModule_01(self):
        u"测试是否显示板块礼品"
        try:
            Common_method.adpass(self,self.driver)
            Common_method.pop_ads(self,self.driver)
            '''点击精明豆tab'''
            self.driver.find_elements_by_id("com.ismartgo.apppub:id/tab_Item_layout")[3].click()
            self.driver.implicitly_wait(5)
            self.driver.find_element_by_id("com.ismartgo.apppub:id/tv_title").click()
            '''查找是否有专区礼品'''
            try:
                loc_text = 'new UiSelector().text("兑换专区")'
                self.driver.find_element_by_android_uiautomator(loc_text)
            except:
                loc_text = 'new UiSelector().text("热门推荐")'
                self.driver.find_element_by_android_uiautomator (loc_text)
            else:
                loc_text = 'new UiSelector().text("热门推荐")'
                self.driver.find_element_by_android_uiautomator(loc_text)
            Common_method.swipe_up(self,self.driver, t=500,n=2)
            time.sleep(1)
            '''查找是否有品类礼品'''
            self.driver.find_element_by_id("com.ismartgo.apppub:id/tv_more_gifts")
            Common_method.swipe_up(self, self.driver, t=500, n=3)
            self.driver.find_element_by_id("com.ismartgo.apppub:id/tv_more_gifts")
            self.driver.find_element_by_id("com.ismartgo.apppub:id/tv_left").click()
            self.assertEqual(self.driver.current_activity,"com.ismartgo.app.activity.Tab_Container_Activity")
        except:
            Common_method.cutScreenShot(self,self.driver,"是否显示板块礼品")
            self.assertTrue(None,"执行失败，请查看截图")
    def test_giftModule_02(self):
        u"测试搜索礼品"
        try:
            Common_method.adpass(self,self.driver)
            Common_method.pop_ads(self,self.driver)
            '''点击精明豆tab'''
            self.driver.find_elements_by_id("com.ismartgo.apppub:id/tab_Item_layout")[3].click()
            self.driver.implicitly_wait(5)
            self.driver.find_element_by_id("com.ismartgo.apppub:id/tv_title").click()
            '''点击搜索框'''
            self.driver.find_element_by_id("com.ismartgo.apppub:id/iv_right").click()
            '''输入购物卡，点击搜索'''
            self.driver.find_element_by_id("com.ismartgo.apppub:id/et_search").send_keys("购物卡")
            self.driver.find_element_by_id("com.ismartgo.apppub:id/tv_search").click()
            assertName = self.driver.find_element_by_id("com.ismartgo.apppub:id/tv_class").text
            '''检查搜索结果页面，筛选框选项'''
            self.assertEqual(assertName,"购物卡")
            self.driver.find_element_by_id("com.ismartgo.apppub:id/pv_back").click()
            self.assertEqual(self.driver.current_activity,"com.ismartgo.app.activity.GiftExchangeActivity")
        except:
            Common_method.cutScreenShot (self, self.driver, "搜索礼品")
            self.assertTrue (None, "执行失败，请查看截图")

    def test_giftModule_03(self):
        u"测试查看更多礼品"
        try:
            Common_method.adpass(self,self.driver)
            Common_method.pop_ads(self,self.driver)
            '''点击精明豆tab'''
            self.driver.find_elements_by_id("com.ismartgo.apppub:id/tab_Item_layout")[3].click()
            self.driver.implicitly_wait(5)
            self.driver.find_element_by_id("com.ismartgo.apppub:id/tv_title").click()
            '''查找是否有专区礼品'''
            try:
                Common_method.swipe_up(self,self.driver, t=500,n=2)
            except:
                Common_method.swipe_up(self, self.driver, t=500, n=2)   #上滑出错时，再次重试上滑
            '''点击更多'''
            self.driver.find_element_by_id("com.ismartgo.apppub:id/tv_more_gifts").click()
            self.driver.find_element_by_id("com.ismartgo.apppub:id/tv_beans").click()
            '''选择豆子范围'''
            self.driver.find_element_by_id("com.ismartgo.apppub:id/tv_name").click()
            time.sleep(2)
            self.driver.find_element_by_id("com.ismartgo.apppub:id/pv_back").click()
            self.assertEqual(self.driver.current_activity, "com.ismartgo.app.activity.GiftExchangeActivity")
        except:
            Common_method.cutScreenShot(self,self.driver,"查看更多礼品")
            self.assertTrue(None,"执行失败，请查看截图")

    def test_giftModule_04(self):
        u"测试查看礼品详情"
        try:
            Common_method.adpass(self,self.driver)
            Common_method.pop_ads(self,self.driver)
            '''点击精明豆tab'''
            self.driver.find_elements_by_id("com.ismartgo.apppub:id/tab_Item_layout")[3].click()
            self.driver.implicitly_wait(5)
            self.driver.find_element_by_id("com.ismartgo.apppub:id/tv_title").click()
            try:
                '''如果有vip板块礼品，点击礼品'''
                loc_text_vip = 'new UiSelector().text("VIP专属")'
                self.driver.find_element_by_android_uiautomator(loc_text_vip).click()
            except:
                '''没有专区礼品，检查是否有推荐礼品'''
                loc_text_hot = 'new UiSelector().text("热门单品")'
                self.driver.find_element_by_android_uiautomator(loc_text_hot).click()
                '''查看礼品详情后返回礼品列表'''
                self.driver.find_element_by_id ("com.ismartgo.apppub:id/tv_left").click ()
                self.assertEqual (self.driver.current_activity, "com.ismartgo.app.activity.GiftExchangeActivity")
            else:
                '''查看vip礼品详情'''
                self.driver.find_element_by_id("com.ismartgo.apppub:id/iv_logo").click()
                self.driver.find_element_by_id("com.ismartgo.apppub:id/tv_left").click()
                self.driver.find_element_by_id("com.ismartgo.apppub:id/tv_left").click()
                self.assertEqual(self.driver.current_activity,"com.ismartgo.app.activity.GiftExchangeActivity")
                loc_text_hot = 'new UiSelector().text("热门单品")'
                self.driver.find_element_by_android_uiautomator(loc_text_hot).click()
                self.driver.find_element_by_id ("com.ismartgo.apppub:id/tv_left").click ()
                self.assertEqual (self.driver.current_activity, "com.ismartgo.app.activity.GiftExchangeActivity")
            try:
                Common_method.swipe_up(self,self.driver, t=500,n=3)
            except:
                Common_method.swipe_up (self, self.driver, t=500, n=3)
            self.driver.find_element_by_id("com.ismartgo.apppub:id/iv_logo").click()
            self.driver.find_element_by_id("com.ismartgo.apppub:id/tv_left").click()
            self.assertEqual(self.driver.current_activity,"com.ismartgo.app.activity.GiftExchangeActivity")
        except:
            Common_method.cutScreenShot(self,self.driver,"查看礼品详情")
            self.assertTrue(None,"执行失败，请查看截图")

    def test_exchangeGift(self):
        u"测试兑换礼品"
        try:
            Common_method.adpass(self,self.driver)
            Common_method.pop_ads(self,self.driver)
            '''点击精明豆tab'''
            self.driver.find_elements_by_id("com.ismartgo.apppub:id/tab_Item_layout")[3].click()
            self.driver.implicitly_wait(5)
            self.driver.find_element_by_id("com.ismartgo.apppub:id/tv_title").click()
            '''点击搜索框'''
            self.driver.find_element_by_id("com.ismartgo.apppub:id/iv_right").click()
            '''输入购物卡，点击搜索'''
            self.driver.find_element_by_id("com.ismartgo.apppub:id/et_search").send_keys("测试")
            self.driver.find_element_by_id ("com.ismartgo.apppub:id/tv_search").click ()
            '''选择第一个礼品'''
            try:
                self.driver.find_elements_by_id("com.ismartgo.apppub:id/iv_logo")[0].click()
            except:
                self.assertTrue(None,"没有测试礼品，无法兑换")
            '''点击立即兑换按钮'''
            self.driver.find_element_by_id("com.ismartgo.apppub:id/btn_confirm").click()
            '''在收件人输入框输入’测试‘'''
            self.driver.find_element_by_id("com.ismartgo.apppub:id/et_addressee").send_keys("测试")
            '''选择地址'''
            self.driver.find_element_by_id("com.ismartgo.apppub:id/et_address").click()
            self.driver.find_element_by_id("com.ismartgo.apppub:id/tv_province").click()
            '''选择省市区'''
            self.driver.find_element_by_id("com.ismartgo.apppub:id/item_text1").click()
            self.driver.find_element_by_id("com.ismartgo.apppub:id/item_text1").click()
            self.driver.find_element_by_id("com.ismartgo.apppub:id/item_text1").click()
            '''有些城市没有四级地址'''
            try:
                self.driver.find_element_by_id("com.ismartgo.apppub:id/item_text1").click()
            except:
                pass
            try:
                Common_method.swipe_up(self,self.driver,t=500,n=2)
            except:
                Common_method.swipe_up(self, self.driver, t=500, n=2)      #上滑出错时，再次重试上滑
            self.driver.find_element_by_id("com.ismartgo.apppub:id/et_detail_address").send_keys("测试")
            '''兑换'''
            self.driver.find_element_by_id("com.ismartgo.apppub:id/btn_confirm_order").click()
            self.driver.find_element_by_id("android:id/button1").click()
            try:
                self.assertEqual(self.driver.current_activity,"com.ismartgo.app.activity.SelectPaymentActivity")
            except:
                self.assertTrue(None,"不是豆+钱礼品，无法跳转到支付页面")
            self.driver.find_element_by_id("com.ismartgo.apppub:id/tv_left").click()
            self.assertEqual(self.driver.current_activity,"com.ismartgo.app.activity.RewardDetailActivity")
        except:
            Common_method.cutScreenShot(self, self.driver, "兑换礼品")
            self.assertTrue (None, "执行失败，请查看截图")







