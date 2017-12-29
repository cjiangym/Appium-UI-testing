#coding:utf-8

from appium import webdriver
import unittest
import time
from common.common_method import Common_method

class MypageTest(unittest.TestCase):

    def setUp(self):
        self.driver = Common_method.setUp(self)
        time.sleep(3)

    def tearDown(self):
        self.driver.quit()

    def test_updateUser(self):
        u"进入修改资料页面"
        try:
            Common_method.adpass(self,self.driver)
            Common_method.pop_ads(self,self.driver)
            '''点击'我'tab'''
            self.driver.find_elements_by_id("com.ismartgo.apppub:id/tab_Item_layout")[4].click()
            self.driver.implicitly_wait(5)
            '''进入修改资料页面'''
            self.driver.find_element_by_id("com.ismartgo.apppub:id/layout_head_logined").click()
            pageTitle = self.driver.find_element_by_id("com.ismartgo.apppub:id/tv_title").text
            self.assertEqual(pageTitle,"我的资料")
            self.driver.find_element_by_id("com.ismartgo.apppub:id/tv_left").click()
            self.assertEqual(self.driver.current_activity,"com.ismartgo.app.activity.Tab_Container_Activity")
        except:
            Common_method.cutScreenShot(self,self.driver,"我的-进入修改资料")
            self.assertTrue(None,"执行失败，请查看截图")

    def test_updateUser_01(self):
        u"修改用户头像-拍照"
        try:
            Common_method.adpass(self,self.driver)
            Common_method.pop_ads(self,self.driver)
            '''点击'我'tab'''
            self.driver.find_elements_by_id("com.ismartgo.apppub:id/tab_Item_layout")[4].click()
            self.driver.implicitly_wait(5)
            '''进入修改资料页面'''
            self.driver.find_element_by_id("com.ismartgo.apppub:id/layout_head_logined").click()
            '''点击头像处'''
            self.driver.find_element_by_id("com.ismartgo.apppub:id/img_head_portrait").click()
            '''选择拍照'''
            self.driver.find_element_by_id("com.ismartgo.apppub:id/photograph").click()
            '''拍照'''
            self.driver.find_element_by_id("com.huawei.camera:id/shutter_button").click()
            '''点击确定照片'''
            self.driver.find_element_by_id("com.huawei.camera:id/btn_done").click()
            '''点击确定图片'''
            self.driver.find_element_by_id("com.ismartgo.apppub:id/id_action_clip").click()
            pageTitle = self.driver.find_element_by_id("com.ismartgo.apppub:id/tv_title").text
            self.assertEqual(pageTitle,"我的资料")
        except:
            Common_method.cutScreenShot(self,self.driver,"拍照修改头像")
            self.assertTrue(None,"执行失败，请查看截图")

    def test_updateUser_02(self):
        u"修改用户头像-从相册选择照片"
        try:
            Common_method.adpass(self,self.driver)
            Common_method.pop_ads(self,self.driver)
            '''点击'我'tab'''
            self.driver.find_elements_by_id("com.ismartgo.apppub:id/tab_Item_layout")[4].click()
            self.driver.implicitly_wait(5)
            '''进入修改资料页面'''
            self.driver.find_element_by_id("com.ismartgo.apppub:id/layout_head_logined").click()
            '''点击头像处'''
            self.driver.find_element_by_id("com.ismartgo.apppub:id/img_head_portrait").click()
            '''选择从相册选择'''
            self.driver.find_element_by_id("com.ismartgo.apppub:id/albums").click()
            '''选择相册'''
            self.driver.find_element_by_id("com.android.gallery3d:id/album_cover_image").click()
            '''选择照片'''
            x = self.driver.find_element_by_id("com.android.gallery3d:id/head_actionmode_title").size["width"]
            y = self.driver.find_element_by_id("com.android.gallery3d:id/head_actionmode_title").size["height"]
            self.driver.tap([(x/2,y*2)],duration=None)
            self.driver.find_element_by_id("com.android.gallery3d:id/head_select_right").click()
            '''点击确定图片'''
            self.driver.find_element_by_id("com.ismartgo.apppub:id/id_action_clip").click()
            pageTitle = self.driver.find_element_by_id("com.ismartgo.apppub:id/tv_title").text
            self.assertEqual(pageTitle,"我的资料")
        except:
            Common_method.cutScreenShot(self,self.driver,"修改头像-从相册选择照片")
            self.assertTrue(None,"执行失败，请查看截图")

    def test_updateUser_03(self):
        u"修改用户昵称"
        try:
            Common_method.adpass(self,self.driver)
            Common_method.pop_ads(self,self.driver)
            '''点击'我'tab'''
            self.driver.find_elements_by_id("com.ismartgo.apppub:id/tab_Item_layout")[4].click()
            self.driver.implicitly_wait(5)
            '''进入修改资料页面'''
            self.driver.find_element_by_id("com.ismartgo.apppub:id/layout_head_logined").click()
            '''点击昵称处'''
            self.driver.find_element_by_id("com.ismartgo.apppub:id/tv_my_nickname").click()
            '''输入昵称'''
            self.driver.find_element_by_id("com.ismartgo.apppub:id/et_info").send_keys("自a动1化~测试")
            '''点击保存'''
            self.driver.find_element_by_id("com.ismartgo.apppub:id/btn_save").click()
            pageTitle = self.driver.find_element_by_id("com.ismartgo.apppub:id/tv_title").text
            self.assertEqual(pageTitle,"我的资料")
        except:
            Common_method.cutScreenShot(self,self.driver,"修改昵称")
            self.assertTrue(None,"执行失败，请查看截图")

    def test_updateUser_04(self):
        u"修改用户昵称-不修改直接返回"
        try:
            Common_method.adpass(self,self.driver)
            Common_method.pop_ads(self,self.driver)
            '''点击'我'tab'''
            self.driver.find_elements_by_id("com.ismartgo.apppub:id/tab_Item_layout")[4].click()
            self.driver.implicitly_wait(5)
            '''进入修改资料页面'''
            self.driver.find_element_by_id("com.ismartgo.apppub:id/layout_head_logined").click()
            '''点击昵称处'''
            self.driver.find_element_by_id("com.ismartgo.apppub:id/tv_my_nickname").click()
            '''点击反回按钮'''
            self.driver.find_element_by_id("com.ismartgo.apppub:id/tv_left").click()
            pageTitle = self.driver.find_element_by_id("com.ismartgo.apppub:id/tv_title").text
            self.assertEqual(pageTitle,"我的资料")
        except:
            Common_method.cutScreenShot(self,self.driver,"修改昵称-不修改直接返回")
            self.assertTrue(None,"执行失败，请查看截图")

    def test_updateUser_05(self):
        u"修改用户生日"
        try:
            Common_method.adpass(self,self.driver)
            Common_method.pop_ads(self,self.driver)
            '''点击'我'tab'''
            self.driver.find_elements_by_id("com.ismartgo.apppub:id/tab_Item_layout")[4].click()
            self.driver.implicitly_wait(5)
            '''进入修改资料页面'''
            self.driver.find_element_by_id("com.ismartgo.apppub:id/layout_head_logined").click()
            '''点击生日处'''
            self.driver.find_element_by_id("com.ismartgo.apppub:id/tv_birthday").click()
            '''点击确定'''
            self.driver.find_element_by_id("com.ismartgo.apppub:id/btn_ok").click()
            pageTitle = self.driver.find_element_by_id("com.ismartgo.apppub:id/tv_title").text
            self.assertEqual(pageTitle,"我的资料")
        except:
            Common_method.cutScreenShot(self,self.driver,"修改用户生日")
            self.assertTrue(None,"执行失败，请查看截图")

    def test_updateUser_06(self):
        u"修改用户性别"
        try:
            Common_method.adpass(self,self.driver)
            Common_method.pop_ads(self,self.driver)
            '''点击'我'tab'''
            self.driver.find_elements_by_id("com.ismartgo.apppub:id/tab_Item_layout")[4].click()
            self.driver.implicitly_wait(5)
            '''进入修改资料页面'''
            self.driver.find_element_by_id("com.ismartgo.apppub:id/layout_head_logined").click()
            '''点击性别处'''
            self.driver.find_element_by_id("com.ismartgo.apppub:id/tv_gender").click()
            '''点击确定'''
            self.driver.find_element_by_id("com.ismartgo.apppub:id/btn_gender_ok").click()
            pageTitle = self.driver.find_element_by_id("com.ismartgo.apppub:id/tv_title").text
            self.assertEqual(pageTitle,"我的资料")
        except:
            Common_method.cutScreenShot(self,self.driver,"修改用户性别")
            self.assertTrue(None,"执行失败，请查看截图")

    def test_updateUser_07(self):
        u"进入更换手机号页面"
        try:
            Common_method.adpass(self,self.driver)
            Common_method.pop_ads(self,self.driver)
            '''点击'我'tab'''
            self.driver.find_elements_by_id("com.ismartgo.apppub:id/tab_Item_layout")[4].click()
            self.driver.implicitly_wait(5)
            '''进入修改资料页面'''
            self.driver.find_element_by_id("com.ismartgo.apppub:id/layout_head_logined").click()
            '''点击手机号处'''
            self.driver.find_element_by_id("com.ismartgo.apppub:id/tv_phone_number").click()
            '''检查页面元素'''
            loc_text_new = 'new UiSelector().text("新号码")'
            self.driver.find_element_by_android_uiautomator (loc_text_new)
            loc_text_valid = 'new UiSelector().text("验证码")'
            self.driver.find_element_by_android_uiautomator (loc_text_new)
            time.sleep(2)
            self.driver.find_element_by_id("com.ismartgo.apppub:id/tv_left").click()
            pageTitle = self.driver.find_element_by_id("com.ismartgo.apppub:id/tv_title").text
            self.assertEqual(pageTitle,"我的资料")
        except:
            Common_method.cutScreenShot(self,self.driver,"进入修改号码页面")
            self.assertTrue(None,"执行失败，请查看截图")

    def test_updateUser_08(self):
        u"修改密码"
        try:
            Common_method.adpass(self,self.driver)
            Common_method.pop_ads(self,self.driver)
            '''点击'我'tab'''
            self.driver.find_elements_by_id("com.ismartgo.apppub:id/tab_Item_layout")[4].click()
            self.driver.implicitly_wait(5)
            '''进入修改资料页面'''
            self.driver.find_element_by_id("com.ismartgo.apppub:id/layout_head_logined").click()
            try:
                '''点击密码处'''
                self.driver.find_element_by_id("com.ismartgo.apppub:id/ll_modify_password").click()
            except:
                self.assertTrue(None,"该账号为微信登录，不能修改密码")
            '''检查页面元素'''
            self.driver.find_element_by_id("com.ismartgo.apppub:id/layout_oldpassword_input").send_keys("123456")
            self.driver.find_element_by_id ("com.ismartgo.apppub:id/layout_password_input").click()
            self.driver.find_element_by_id("com.ismartgo.apppub:id/layout_password_input").send_keys("666666")
            self.driver.find_element_by_id("com.ismartgo.apppub:id/btn_confirm").click()
            pageTitle = self.driver.find_element_by_id("com.ismartgo.apppub:id/tv_title").text
            self.assertEqual(pageTitle,"我的资料")
            '''再次修改密码，还原密码'''
            self.driver.find_element_by_id ("com.ismartgo.apppub:id/ll_modify_password").click()
            self.driver.find_element_by_id ("com.ismartgo.apppub:id/layout_oldpassword_input").send_keys("666666")
            self.driver.find_element_by_id ("com.ismartgo.apppub:id/layout_password_input").click()
            self.driver.find_element_by_id ("com.ismartgo.apppub:id/layout_password_input").send_keys ("123456")
            self.driver.find_element_by_id ("com.ismartgo.apppub:id/btn_confirm").click()
        except:
            Common_method.cutScreenShot(self,self.driver,"修改密码")
            self.assertTrue(None,"执行失败，请查看截图")

    def test_updateUser_09(self):
        u"修改密码-不修改直接返回"
        try:
            Common_method.adpass(self,self.driver)
            Common_method.pop_ads(self,self.driver)
            '''点击'我'tab'''
            self.driver.find_elements_by_id("com.ismartgo.apppub:id/tab_Item_layout")[4].click()
            self.driver.implicitly_wait(3)
            '''进入修改资料页面'''
            self.driver.find_element_by_id("com.ismartgo.apppub:id/layout_head_logined").click()
            try:
                '''点击密码处'''
                self.driver.find_element_by_id("com.ismartgo.apppub:id/ll_modify_password").click()
            except:
                self.assertTrue(None,"该账号为微信登录，不能修改密码")
            '''点击返回按钮'''
            self.driver.find_element_by_id ("com.ismartgo.apppub:id/tv_left").click()
            pageTitle = self.driver.find_element_by_id("com.ismartgo.apppub:id/tv_title").text
            self.assertEqual(pageTitle,"我的资料")
        except:
            Common_method.cutScreenShot(self,self.driver,"修改密码-不修改直接返回")
            self.assertTrue(None,"执行失败，请查看截图")

    def test_updateUser_10(self):
        u"绑定邮箱"
        try:
            Common_method.adpass(self,self.driver)
            Common_method.pop_ads(self,self.driver)
            '''点击'我'tab'''
            self.driver.find_elements_by_id("com.ismartgo.apppub:id/tab_Item_layout")[4].click()
            self.driver.implicitly_wait(3)
            '''进入修改资料页面'''
            self.driver.find_element_by_id("com.ismartgo.apppub:id/layout_head_logined").click()
            '''点击邮箱处'''
            self.driver.find_element_by_id("com.ismartgo.apppub:id/tv_mailbox").click()
            self.driver.find_element_by_id("com.ismartgo.apppub:id/et_email").send_keys("test111@ismartgo.com")
            self.driver.find_element_by_id("com.ismartgo.apppub:id/btn_confirm").click()
            pageTitle = self.driver.find_element_by_id("com.ismartgo.apppub:id/tv_title").text
            self.assertEqual(pageTitle,"我的资料")
        except:
            Common_method.cutScreenShot(self,self.driver,"绑定邮箱")
            self.assertTrue(None,"执行失败，请查看截图")

    def test_updateUser_11(self):
        u"修改地址"
        try:
            Common_method.adpass(self,self.driver)
            Common_method.pop_ads(self,self.driver)
            '''点击'我'tab'''
            self.driver.find_elements_by_id("com.ismartgo.apppub:id/tab_Item_layout")[4].click()
            self.driver.implicitly_wait(5)
            '''进入修改资料页面'''
            self.driver.find_element_by_id("com.ismartgo.apppub:id/layout_head_logined").click()
            '''点击地址处'''
            self.driver.find_element_by_id("com.ismartgo.apppub:id/tv_my_address").click()
            self.driver.find_element_by_id("com.ismartgo.apppub:id/et_name").send_keys("测~试a")
            self.driver.find_element_by_id("com.ismartgo.apppub:id/et_phone").send_keys("11111111111")
            '''选择省市区'''
            self.driver.find_element_by_id("com.ismartgo.apppub:id/tv_address").click()
            self.driver.find_element_by_id("com.ismartgo.apppub:id/tv_province").click()
            self.driver.find_element_by_id("com.ismartgo.apppub:id/item_text1").click()
            self.driver.find_element_by_id("com.ismartgo.apppub:id/item_text1").click()
            self.driver.find_element_by_id ("com.ismartgo.apppub:id/item_text1").click()
            try:
                self.driver.find_element_by_id ("com.ismartgo.apppub:id/item_text1").click()
                '''有些城市没有四级地址'''
            except:
                pass
            self.driver.find_element_by_id("com.ismartgo.apppub:id/et_detail_address").send_keys("详细地址测试")
            self.driver.find_element_by_id("com.ismartgo.apppub:id/btn_submit").click()
            pageTitle = self.driver.find_element_by_id("com.ismartgo.apppub:id/tv_title").text
            self.assertEqual(pageTitle,"我的资料")
        except:
            Common_method.cutScreenShot(self,self.driver,"修改地址")
            self.assertTrue(None,"执行失败，请查看截图")

    def test_updateUser_12(self):
        u"修改资料-邀请码检查"
        try:
            Common_method.adpass(self,self.driver)
            Common_method.pop_ads(self,self.driver)
            '''点击'我'tab'''
            self.driver.find_elements_by_id("com.ismartgo.apppub:id/tab_Item_layout")[4].click()
            self.driver.implicitly_wait(5)
            '''进入修改资料页面'''
            self.driver.find_element_by_id("com.ismartgo.apppub:id/layout_head_logined").click()
            '''点击邀请码处'''
            self.driver.find_element_by_id("com.ismartgo.apppub:id/tv_invitate_code").click()
            assert1 = self.driver.find_element_by_id("com.ismartgo.apppub:id/tv_invitate_code_tips").text
            self.assertEqual(assert1,"我的邀请码")
            assert2 = 'new UiSelector().text("好友邀请码")'
            self.driver.find_element_by_android_uiautomator(assert2)
            self.driver.find_element_by_id("com.ismartgo.apppub:id/tv_left").click()
            pageTitle = self.driver.find_element_by_id("com.ismartgo.apppub:id/tv_title").text
            self.assertEqual(pageTitle,"我的资料")
        except:
            Common_method.cutScreenShot(self,self.driver,"修改资料-邀请码检查")
            self.assertTrue(None,"执行失败，请查看截图")

    def test_enterForum_01(self):
        u"测试进入社区页面"
        try:
            Common_method.adpass (self, self.driver)
            Common_method.pop_ads (self, self.driver)
            '''点击'我'tab'''
            self.driver.find_elements_by_id ("com.ismartgo.apppub:id/tab_Item_layout")[4].click ()
            self.driver.implicitly_wait(5)
            self.driver.find_element_by_id("com.ismartgo.apppub:id/layout_recommend").click()
            pageTitle = self.driver.find_element_by_id("com.ismartgo.apppub:id/tv_title").text
            pageCorner = self.driver.find_element_by_id("com.ismartgo.apppub:id/tv_right").text
            self.assertEqual(pageTitle,"社区")
            self.assertEqual(pageCorner,"我的互动")
            self.driver.find_element_by_id("com.ismartgo.apppub:id/tv_left").click()
            self.assertEqual(self.driver.current_activity,"com.ismartgo.app.activity.Tab_Container_Activity")
        except:
            Common_method.cutScreenShot(self,self.driver,"我的-进入社区")
            self.assertTrue(None,"执行失败，请查看截图")

    def test_enterForum_02(self):
        u"测试从去看看进入社区页面"
        try:
            Common_method.adpass (self, self.driver)
            Common_method.pop_ads (self, self.driver)
            '''点击'我'tab'''
            self.driver.find_elements_by_id ("com.ismartgo.apppub:id/tab_Item_layout")[4].click ()
            self.driver.implicitly_wait(5)
            Common_method.swipe_up(self,self.driver,t=500,n=1)
            self.driver.find_element_by_id("com.ismartgo.apppub:id/layout_community").click()
            pageTitle = self.driver.find_element_by_id("com.ismartgo.apppub:id/tv_title").text
            pageCorner = self.driver.find_element_by_id("com.ismartgo.apppub:id/tv_right").text
            self.assertEqual(pageTitle,"社区")
            self.assertEqual(pageCorner,"我的互动")
            self.driver.find_element_by_id("com.ismartgo.apppub:id/tv_left").click()
            self.assertEqual(self.driver.current_activity,"com.ismartgo.app.activity.Tab_Container_Activity")
        except:
            Common_method.cutScreenShot(self,self.driver,"我的-去看看-进入社区")
            self.assertTrue(None,"执行失败，请查看截图")