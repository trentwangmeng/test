# -*- coding: utf-8 -*-
import Page
from Base.AppBase import BasePage
from selenium.webdriver.common.by import By
from appium.webdriver.common.touch_action import TouchAction
from Utils.tool_log import logger

log = logger()
class DouYinLikePage():
    """
    以单个页面为对象，将针对该页面的操作都集中在这里
    APP
    """
    def __init__(self,phone_name):
        self.base = BasePage(phone_name)
        self.driver = self.base.driver

    def Loggin(self):
        log.info("请等待一分钟左右")
        self.base.wait_second(1,10)
        try:
            self.base.find_element(By.XPATH,'//*[@text="我知道了"]').click()

        except:
            try:
                self.base.find_element(By.XPATH, '//*[@text="以后再说"]').click()
            except:
                pass

        self.base.find_element(By.XPATH,'//*[@text="消息"]').click()
        log.info("打开聊天记录")
        self.base.find_element(By.XPATH,'//*[@resource-id="com.ss.android.ugc.aweme:id/6-" and @class="android.widget.ImageView"]').click()
        # self.base.find_element(By.XPATH,'//*[@resource-id="com.ss.android.ugc.aweme:id/63" and @class="com.bytedance.ies.dmt.ui.widget.DmtTextView"]').click()

        log.info('检查用户昵称')
        contacts = self.base.find_element(By.ID,'com.ss.android.ugc.aweme:id/bp')
        contacts_name = contacts.text
        if contacts_name == "_":
            pass
        else:
            log.info("昵称改为：%s" % contacts_name)

        log.info('查看用户是否在线')
        status = self.base.find_element(By.ID,'com.ss.android.ugc.aweme:id/d23')
        contacts_status = status.text
        log.info(" %s %s",contacts_name,contacts_status)
        self.base.save_screenshot("用户状态截图")

        log.info("打开联系人详情")
        self.base.find_element(By.XPATH,'//android.widget.LinearLayout[@content-desc="更多"]/android.widget.ImageView').click()

        log.info("打开联系人主页")
        self.base.find_element(By.XPATH,'//com.bytedance.ies.dmt.ui.widget.DmtTextView[@content-desc="{name}"]'.format(name=contacts_name)).click()

        log.info("查看主页")
        #年龄
        age = self.base.find_element(By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.HorizontalScrollView/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout[1]/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.TextView[1]').text

        #地区
        address = self.base.find_element(By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.HorizontalScrollView/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout[1]/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.TextView[2]').text

        # 获赞数
        praised = self.base.find_element(By.ID,'com.ss.android.ugc.aweme:id/b_t')
        praised_number = int(praised.text)

        # 关注数
        attention = self.base.find_element(By.ID,'com.ss.android.ugc.aweme:id/dhp')
        attention_number = int(attention.text)

        # 粉丝数
        fans = self.base.find_element(By.ID,'com.ss.android.ugc.aweme:id/dhh')
        fans_number = int(fans.text)

        # 作品数
        works = self.base.find_element(By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.HorizontalScrollView/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout[1]/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.HorizontalScrollView/android.widget.LinearLayout/androidx.appcompat.app.a.b[1]/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.TextView')
        works_text = works.get_attribute("text")
        works_number = int(works_text[2:])

        # 喜欢数
        praise = self.base.find_element(By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.HorizontalScrollView/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout[1]/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.HorizontalScrollView/android.widget.LinearLayout/androidx.appcompat.app.a.b[2]/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.TextView')
        praise_text = praise.text
        # praise_text2 = praise.get_attribute("text")
        praise_number = int(praise_text[2:])

        self.base.save_screenshot("用户主页截图")

        # log.info('%s当前获赞%S个，关注%s个，粉丝%s个，作品%s个，喜欢%s个作品',contacts_name,praised_number,attention_number,fans_number,works_number,praise_number)
        log.info('{}{}，{}人，当前获赞{}次，关注{}人，粉丝{}人，作品{}个，喜欢{}个作品'.format(contacts_name,age,address,praised_number,attention_number,fans_number,works_number,praise_number))

        # 获赞数量变化
        praised_change_number = praised_number - 18
        if praised_change_number == 0:
            log.info('%s的获赞数量没有变化',contacts_name)
        elif praised_change_number > 0:
            log.info('%s增加获赞%s次',contacts_name,praised_change_number)
        else:
            log.info('%s减少获赞%s次',contacts_name,praised_change_number)

        # 关注数量变化
        attention_change_number = attention_number - 49
        if attention_change_number == 0:
            log.info('%s的关注数量没有变化',contacts_name)
        elif attention_change_number > 0:
            log.info('%s新关注%s人',contacts_name,attention_change_number)
        else:
            log.info('%s减少关注%s人',contacts_name,attention_change_number)

        # 粉丝数量变化
        fans_change_number = fans_number - 8
        if fans_change_number == 0:
            log.info('%s的粉丝数量没有变化',contacts_name)
        elif fans_change_number > 0:
            log.info('%s增加粉丝%s人',contacts_name,fans_change_number)
        else:
            log.info('%s减少粉丝%s人', contacts_name, fans_change_number)

        # 作品数量变化
        works_change_number = works_number - 5
        if works_change_number == 0:
            log.info('%s的作品数量没有变化',contacts_name)
        elif works_change_number > 0:
            log.info('%s新增作品%s个',contacts_name,works_change_number)
        else:
            log.info('%s减少作品%s个',contacts_name,works_change_number)

        # 喜欢数量变化
        praise_change_number = praise_number - 544
        if praise_change_number == 0:
            log.info('%s的喜欢数量没有变化',contacts_name)
        elif praise_change_number > 0:
            log.info('%s增加喜欢%s个',contacts_name,praise_change_number)
        else:
            log.info('%s取消喜欢%s个', contacts_name, praise_change_number)

        # self.base.find_element(By.ID, 'com.ss.android.ugc.aweme:id/bp')
        # self.driver.find_element_by_xpath('')
        # self.driver.find_element_by_xpath('')
        # self.driver.find_element_by_xpath('')
        # self.driver.find_element_by_xpath('')
        # self.driver.find_element_by_xpath('')
        # self.driver.find_element_by_xpath('')
        # self.driver.find_element_by_xpath('')
        #

