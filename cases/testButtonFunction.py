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

    def test_clickHomepagebutton_01(self):
        u"点击首页到店签到-签到"
        result = False
        try:
            try:
                self.common_method.adpass(self.driver)
                self.common_method.pop_ads(self.driver)
                self.driver.find_element_by_name("到店签到").click()
                time.sleep (5)
                pageName = self.driver.find_element_by_id("com.ismartgo.apppub:id/tv_title").text
                self.assertEqual(pageName,"到店签到")
                #找签到按钮
                signButton = self.driver.find_element_by_xpath("//android.support.v7.widget.RecyclerView/android.widget.LinearLayout[1]/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.LinearLayout[2]")
                canSign =signButton.is_enabled()
                if canSign:             #如果签到按钮是可签到状态，则签到，否则直接返回上一级页面
                    signButton.click()
                    time.sleep(5)
                    self.driver.find_element_by_id ("com.ismartgo.apppub:id/iv_left").click()
                    self.driver.find_element_by_id ("com.ismartgo.apppub:id/pv_back").click()
                else:
                    self.driver.find_element_by_id("com.ismartgo.apppub:id/pv_back").click()
            except:
                signButton = self.driver.find_element_by_id("com.ismartgo.apppub:id/store_signin")
                self.driver.find_element_by_id ("com.ismartgo.apppub:id/pv_back").click()
        except:
            self.common_method.cutScreenShot("test_ClickShopSign" + "_" + self.common_method.timestamp)
            self.assertEqual (result, "执行失败，请查看截图")
        self.assertEqual(self.driver.current_activity,"com.ismartgo.app.activity.Tab_Container_Activity")

    def test_clickHomepagebutton_02(self):
        u"点击首页拍立赚按钮"
        result = False
        try:
            self.common_method.adpass(self.driver)
            self.common_method.pop_ads(self.driver)
            button_list = self.driver.find_elements_by_id("com.ismartgo.apppub:id/iv_head_img")
            button_list[1].click()                              #点击拍立赚按钮
            time.sleep(5)
            self.pageName = self.driver.find_element_by_id("com.ismartgo.apppub:id/rb_all").text
        except:
            self.common_method.cutScreenShot ("test_clickzbgame" + "_" + self.common_method.timestamp)
            self.assertEqual(result, "执行失败，请查看截图")
        else:
            self.assertEqual (self.pageName, "全部")
            self.driver.find_element_by_id ("com.ismartgo.apppub:id/tv_left").click()
        self.assertEqual(self.driver.current_activity, "com.ismartgo.app.activity.Tab_Container_Activity")


    def test_clickHomepagebutton_03(self):
        u"点击首页小票记账按钮"
        result = False
        try:
            self.common_method.adpass(self.driver)
            self.common_method.pop_ads(self.driver)
            button_list = self.driver.find_elements_by_id ("com.ismartgo.apppub:id/iv_head_img")
            button_list[2].click ()                             #点击小票记账按钮
            time.sleep(2)
            self.driver.find_element_by_id("com.ismartgo.apppub:id/iv_receipt_back").click()
        except:
            self.common_method.cutScreenShot("test_ClickShopSign"+"_"+self.common_method.timestamp)
            self.assertEqual(result,"执行失败，请查看截图")
        self.assertEqual(self.driver.current_activity, "com.ismartgo.app.activity.Tab_Container_Activity")

    def test_clickHomepagebutton_04(self):
        u"点击首页扫描商品按钮"
        result = False
        try:
            self.common_method.adpass(self.driver)
            self.common_method.pop_ads(self.driver)
            button_list = self.driver.find_elements_by_id ("com.ismartgo.apppub:id/iv_head_img")
            button_list[3].click ()          # 点击扫描商品按钮
            time.sleep (5)
            self.pageName = self.driver.find_element_by_id ("com.ismartgo.apppub:id/tv_title").text
        except:
            self.common_method.cutScreenShot ("test_clickScangoods" + "_" + self.common_method.timestamp)
            self.assertEqual (result, "执行失败，请查看截图")
        else:
            self.assertEqual (self.pageName, "商品扫描")
            self.driver.find_element_by_id ("com.ismartgo.apppub:id/tv_left").click ()
        self.assertEqual (self.driver.current_activity, "com.ismartgo.app.activity.Tab_Container_Activity")

    def test_clickHomepagebutton_05(self):
        u"点击首页邀请好友按钮"
        result = False
        try:
            self.common_method.adpass(self.driver)
            self.common_method.pop_ads(self.driver)
            button_list = self.driver.find_elements_by_id ("com.ismartgo.apppub:id/iv_head_img")
            button_list[4].click ()          # 点击邀请好友按钮
            time.sleep(2)
            self.pageName = self.driver.find_element_by_id ("com.ismartgo.apppub:id/tv_title").text
        except:
            self.common_method.cutScreenShot ("test_clickScangoods" + "_" + self.common_method.timestamp)
            self.assertEqual(result, "执行失败，请查看截图")
        else:
            self.assertEqual (self.pageName, "邀请好友")
            self.driver.find_element_by_id ("com.ismartgo.apppub:id/tv_left").click ()
        self.assertEqual (self.driver.current_activity, "com.ismartgo.app.activity.Tab_Container_Activity")
    def test_clickHomepagebutton_06(self):
        u"点击首页商城赚按钮"
        result = False
        try:
            self.common_method.adpass(self.driver)
            self.common_method.pop_ads(self.driver)
            button_list = self.driver.find_elements_by_id ("com.ismartgo.apppub:id/iv_head_img")
            button_list[5].click()          # 点击商城赚按钮
            self.driver.implicitly_wait(8)
            self.pageName = self.driver.find_element_by_id ("com.ismartgo.apppub:id/tv_title").text
        except:
            self.common_method.cutScreenShot ("test_clickScangoods" + "_" + self.common_method.timestamp)
            self.assertEqual(result, "执行失败，请查看截图")
        else:
            self.assertEqual (self.pageName, "商城赚")
            self.driver.find_element_by_id ("com.ismartgo.apppub:id/tv_left").click ()
        self.assertEqual (self.driver.current_activity, "com.ismartgo.app.activity.Tab_Container_Activity")

    def test_clickHomepagebutton_07(self):
        u"点击首页超级赚按钮"
        result = False
        try:
            self.common_method.adpass(self.driver)
            self.common_method.pop_ads(self.driver)
            button_list = self.driver.find_elements_by_id ("com.ismartgo.apppub:id/iv_head_img")
            button_list[6].click()          # 点击超级赚按钮
            self.driver.implicitly_wait(8)
            self.pageName = self.driver.find_element_by_id ("com.ismartgo.apppub:id/tv_title").text
        except:
            self.common_method.cutScreenShot ("test_clickHomepagebutton_07" + "_" + self.common_method.timestamp)
            self.assertEqual(result, "执行失败，请查看截图")
        else:
            self.assertEqual (self.pageName, "超级赚")
            self.driver.find_element_by_id ("com.ismartgo.apppub:id/tv_left").click ()
        self.assertEqual (self.driver.current_activity, "com.ismartgo.app.activity.Tab_Container_Activity")

    def test_clickHomepagebutton_08(self):
        u"点击首页淘宝赚按钮"
        result = False
        try:
            self.common_method.adpass(self.driver)
            self.common_method.pop_ads(self.driver)
            button_list = self.driver.find_elements_by_id ("com.ismartgo.apppub:id/iv_head_img")
            button_list[7].click()           # 点击淘宝赚按钮
            self.driver.implicitly_wait(8)
            self.pageName = self.driver.find_element_by_id ("com.ismartgo.apppub:id/tv_title").text
        except:
            self.common_method.cutScreenShot ("test_clickHomepagebutton_08" + "_" + self.common_method.timestamp)
            self.assertEqual(result, "执行失败，请查看截图")
        else:
            self.assertEqual (self.pageName, "淘宝赚")
            self.driver.find_element_by_id ("com.ismartgo.apppub:id/tv_left").click ()
        self.assertEqual (self.driver.current_activity, "com.ismartgo.app.activity.Tab_Container_Activity")

    def test_clickHomepagebutton_09(self):
        u"点击首页超值购物卡按钮"
        result = False
        try:
            self.common_method.adpass(self.driver)
            self.common_method.pop_ads(self.driver)
            button_list = self.driver.find_elements_by_id ("com.ismartgo.apppub:id/iv_head_img")
            button_list[8].click()           # 超值购物卡
            time.sleep(2)
            self.activity = self.driver.current_activity
        except:
            self.common_method.cutScreenShot ("test_clickHomepagebutton_08" + "_" + self.common_method.timestamp)
            self.assertEqual(result, "执行失败，请查看截图")
        else:
            self.assertEqual (self.activity, "com.ismartgo.app.activity.RewardExchangeActivity")
            self.driver.find_element_by_id ("com.ismartgo.apppub:id/pv_back").click ()
        self.assertEqual (self.driver.current_activity, "com.ismartgo.app.activity.Tab_Container_Activity")

    def test_clickHomepagebutton_10(self):
        u"点击首页礼品商城按钮"
        result = False
        try:
            self.common_method.adpass(self.driver)
            self.common_method.pop_ads(self.driver)
            button_list = self.driver.find_elements_by_id ("com.ismartgo.apppub:id/iv_head_img")
            button_list[9].click()           # 超值购物卡
            time.sleep(2)
            self.pageName = self.driver.find_element_by_id("com.ismartgo.apppub:id/tv_title").text
        except:
            self.common_method.cutScreenShot ("test_clickHomepagebutton_08" + "_" + self.common_method.timestamp)
            self.assertEqual(result, "执行失败，请查看截图")
        else:
            self.assertEqual(self.pageName, "礼品兑换")
            self.driver.find_element_by_id ("com.ismartgo.apppub:id/tv_left").click()
        self.assertEqual(self.driver.current_activity, "com.ismartgo.app.activity.Tab_Container_Activity")

    def test_clickHomepagebutton_11(self):
        u"点击我的页面我的兑换"
        result = False
        try:
            self.common_method.adpass(self.driver)
            self.common_method.pop_ads(self.driver)
            tab_button_list = self.driver.find_elements_by_id ("com.ismartgo.apppub:id/tab_Item_layout")
            tab_button_list[4].click()           # 点击tab按钮“我”
            button_list = self.driver.find_elements_by_id("com.ismartgo.apppub:id/iv_btn_pic")
            button_list[0].click()
            time.sleep(3)
            self.pageName = self.driver.find_element_by_id("com.ismartgo.apppub:id/tv_title").text
        except:
            self.common_method.cutScreenShot ("test_clickHomepagebutton_11" + "_" + self.common_method.timestamp)
            self.assertEqual(result, "执行失败，请查看截图")
        else:
            self.assertEqual(self.pageName,"我的兑换")
            self.driver.find_element_by_id ("com.ismartgo.apppub:id/tv_left").click()
        self.assertEqual(self.driver.current_activity, "com.ismartgo.app.activity.Tab_Container_Activity")
    def test_clickHomepagebutton_12(self):
        u"点击我的页面网购订单"
        result = False
        try:
            self.common_method.adpass(self.driver)
            self.common_method.pop_ads(self.driver)
            tab_button_list = self.driver.find_elements_by_id ("com.ismartgo.apppub:id/tab_Item_layout")
            tab_button_list[4].click()           # 点击tab按钮“我”
            button_list = self.driver.find_elements_by_id("com.ismartgo.apppub:id/iv_btn_pic")
            button_list[1].click()               #点击网购订单
            time.sleep(3)
            self.pageName = self.driver.find_element_by_id("com.ismartgo.apppub:id/tv_title").text
        except:
            self.common_method.cutScreenShot ("test_clickHomepagebutton_12" + "_" + self.common_method.timestamp)
            self.assertEqual(result, "执行失败，请查看截图")
        else:
            self.assertEqual(self.pageName,"我的订单")
            self.driver.find_element_by_id ("com.ismartgo.apppub:id/tv_left").click()
        self.assertEqual(self.driver.current_activity, "com.ismartgo.app.activity.Tab_Container_Activity")

    def test_clickHomepagebutton_13(self):
        u"点击我的页面我的关注"
        result = False
        try:
            self.common_method.adpass(self.driver)
            self.common_method.pop_ads(self.driver)
            tab_button_list = self.driver.find_elements_by_id ("com.ismartgo.apppub:id/tab_Item_layout")
            tab_button_list[4].click()           # 点击tab按钮“我”
            button_list = self.driver.find_elements_by_id("com.ismartgo.apppub:id/iv_btn_pic")
            button_list[2].click()               #点击我的关注
            time.sleep(3)
            self.pageName = self.driver.find_element_by_id("com.ismartgo.apppub:id/tv_title").text
        except:
            self.common_method.cutScreenShot ("test_clickHomepagebutton_12" + "_" + self.common_method.timestamp)
            self.assertEqual(result, "执行失败，请查看截图")
        else:
            self.assertEqual(self.pageName,"我的关注")
            self.driver.find_element_by_id ("com.ismartgo.apppub:id/tv_left").click()
        self.assertEqual(self.driver.current_activity, "com.ismartgo.app.activity.Tab_Container_Activity")
    def test_clickHomepagebutton_14(self):
        u"点击我的页面我的卡券"
        result = False
        try:
            self.common_method.adpass(self.driver)
            self.common_method.pop_ads(self.driver)
            tab_button_list = self.driver.find_elements_by_id ("com.ismartgo.apppub:id/tab_Item_layout")
            tab_button_list[4].click()           # 点击tab按钮“我”
            button_list = self.driver.find_elements_by_id("com.ismartgo.apppub:id/iv_btn_pic")
            button_list[3].click()               #点击我的卡券
            time.sleep(3)
            self.pageName = self.driver.find_element_by_id("com.ismartgo.apppub:id/tv_title").text
        except:
            self.common_method.cutScreenShot ("test_clickHomepagebutton_12" + "_" + self.common_method.timestamp)
            self.assertEqual(result, "执行失败，请查看截图")
        else:
            self.assertEqual(self.pageName,"我的卡劵")
            self.driver.find_element_by_id ("com.ismartgo.apppub:id/tv_left").click()
        self.assertEqual(self.driver.current_activity, "com.ismartgo.app.activity.Tab_Container_Activity")
    def test_clickHomepagebutton_15(self):
        u"点击我的页面购物清单"
        result = False
        try:
            self.common_method.adpass(self.driver)
            self.common_method.pop_ads(self.driver)
            tab_button_list = self.driver.find_elements_by_id ("com.ismartgo.apppub:id/tab_Item_layout")
            tab_button_list[4].click()           # 点击tab按钮“我”
            button_list = self.driver.find_elements_by_id("com.ismartgo.apppub:id/iv_btn_pic")
            button_list[4].click()               #点击购物清单
            time.sleep(3)
            self.pageName = self.driver.find_element_by_id("com.ismartgo.apppub:id/tv_title").text
        except:
            self.common_method.cutScreenShot ("test_clickHomepagebutton_12" + "_" + self.common_method.timestamp)
            self.assertEqual(result, "执行失败，请查看截图")
        else:
            self.assertEqual(self.pageName,"购物清单")
            self.driver.find_element_by_id ("com.ismartgo.apppub:id/tv_left").click()
        self.assertEqual(self.driver.current_activity, "com.ismartgo.app.activity.Tab_Container_Activity")