# -*- encoding: utf-8 -*-
'''
@File    :   BasePage.py
@Time    :   2020/02/11 14:49:52
@Author  :   peace_su
@Version :   1.0

'''

# here put the import lib
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.touch_action import TouchAction
import time
import datetime
from appium import webdriver
from Utils.YamlMethod import XiaoMaUtils
from Config.config import SCREENSHOT_DIR
import os
import allure
from Utils.tool_log import logger
from datetime import datetime


class BasePage(object):
    """
    类注释
    详细描述
    Attributes:
        属性说明
    """
    def __init__(self, phone_name):
        """
        Class1类初始化方法
        Args:
            paramter1: 入参说明
            paramter2: 入参说明
        """
        self.logger = logger()
        url = ""
        capabilities = {}
        # 设备信息
        date = XiaoMaUtils.read_yaml_file("phone.yaml")["devices"]
        for i in range(len(date)):
            if date[i]["name"] == phone_name:
                url = date[i]["url"]
                self.logger.debug("uri:%s", url)
                capabilities = date[i]["capabilities"]
                self.logger.debug("capabilities:%s", capabilities)


        # 声明我们的driver对象
        self.driver = webdriver.Remote(url, capabilities)

    def find_element(self, *loc):
        '''
        重写查找单个元素方法
        '''
        self.logger.debug("执行 BasePage.find_element(%s)", loc[1])
        try:
            self.logger.debug("执行 WebDriverWait(self.driver, 5, 0.5).until(EC.visibility_of_element_located(%s)) ", loc[1])
            WebDriverWait(self.driver, 5, 0.5).until(
                EC.visibility_of_element_located(loc))                 # 入参本身是元组，不需要加*
            self.logger.debug("执行 self.driver.find_elements(%s)", loc[1])
            return self.driver.find_element(*loc)                     #注意：入参为元组的元素，需要加*。Python存在这种特性，就是将入参放在元组里。
        except Exception:
            self.logger.error('未找到元素：%s 请检查！' % loc[1])
            self.save_screenshot('未通过%s找到元素'% loc[0])

    def find_elements(self, *loc):
        '''
        重写查找多个元素方法
        '''
        self.logger.debug("执行 BasePage.find_elements(%s)", loc[1])
        try:
            self.logger.debug("执行 WebDriverWait(self.driver, 5, 0.5).until(EC.visibility_of_element_located(%s)) ", loc[1])
            WebDriverWait(self.driver, 5, 0.5).until(
                EC.visibility_of_element_located(loc))
            self.logger.debug("执行 self.driver.find_elements(%s)",loc[1])
            return self.driver.find_elements(*loc)
        except AttributeError:
            self.logger.error('未找到元素：%s 请检查！' % loc[1])
            self.save_screenshot('未通过%s找到元素'% loc[0])

    def send_keys(self, loc, vaule, clear_first=True, click_first=True):
        '''
        重写send_keys方法
        '''
        self.logger.debug("执行 BasePage.send_keys(%s%s%s%s%s)", loc[1],vaule,clear_first,click_first)
        try:
            self.logger.debug("loc = getattr(self,_%s )", loc[1])
            loc = getattr(self, "_%s" % loc)  # getattr相当于实现self.loc
            if click_first:
                self.logger.debug("click_first=True")
                self.logger.debug("self.find_element(%s).click()", loc[1])
                self.find_element(*loc).click()
            if clear_first:
                self.logger.debug("clear_first=True")
                self.logger.debug("self.find_element(%s).clear()", loc[1])
                self.find_element(*loc).clear()
                self.logger.debug("self.find_element(%s).send_keys(%s)", loc[1],vaule)
                self.find_element(*loc).send_keys(vaule)
        except AttributeError:
            self.logger.error('未找到元素：%s 请检查！' % loc[1])
            self.save_screenshot('未通过%s找到元素'% loc[0])

    def is_toast_exist(self, text):
        '''is toast exist, return True or False
        :Agrs:
            - text   - 页面上看到的文本内容
        :Usage:
            is_toast_exist("看到的内容")
        '''
        self.logger.debug("BasePage.is_toast_exist(%s)", text)
        try:
            self.logger.debug("toast_loc = (By.XPATH, './/*[contains(@text,'%s')]')", text)
            # self.logger.debug(r"toast_loc = (By.XPATH, './/*[contains(@text,'%s')]')", text) 与上面一样
            toast_loc = (By.XPATH, ".//*[contains(@text,'%s')]" % text)
            self.logger.debug("WebDriverWait(self.driver, 5, 0.5).until(EC.visibility_of_element_located(%s)) ", toast_loc)
            WebDriverWait(self.driver, 5, 0.5).until(
                EC.presence_of_element_located(toast_loc))
            self.logger.debug("BasePage.is_toast_exist(%s):True", text)
            return True
        except Exception as e:
            self.logger.debug("%s", e)
            self.logger.error('未找到文本：%s 请检查！' % text)
            self.save_screenshot('未找到文本：%s' % text)
            self.logger.debug("BasePage.is_toast_exist(%s):False", text)
            return False

    def is_element_exist(self, *loc):
        self.logger.debug("BasePage.is_element_exist(%s)", loc[1])
        try:
            self.logger.debug("WebDriverWait(self.driver, 5, 0.5).until(EC.visibility_of_element_located(%s)) ", loc[1])
            WebDriverWait(self.driver, 5, 0.5).until(
                EC.visibility_of_element_located(loc))
            self.logger.debug("self.driver.find_elements(%s)",loc[1])
            self.driver.find_element(*loc)
            self.logger.debug("BasePage.is_element_exist(%s):True", loc[1])
            return True
        except Exception:
            self.logger.debug("BasePage.is_element_exist(%s):False", loc[1])
            self.logger.error('未找到元素：%s 请检查！' % loc[1])
            self.save_screenshot('未通过%s找到元素'% loc[0])
            return False

    def get_size(self):
        '''获取屏幕大小
        '''
        self.logger.debug("BasePage.get_size()")
        try:
            self.logger.debug("size = self.driver.get_window_size()")
            size = self.driver.get_window_size()
            self.logger.debug("BasePage.get_size()--%s",size)
            return size
        except Exception:
            self.save_screenshot('无法获取屏幕大小')
            self.logger.debug("无法获取屏幕大小")
            return None

    def swipe_to_left(self):
        """
        左滑
        """
        window_size = self.get_size()
        width = window_size.get("width")
        height = window_size.get("height")
        try:
            self.driver.swipe(width*0.9, height*0.5, width*0.1, height*0.5)
            time.sleep(0.5)
        except Exception:
            self.save_screenshot('无法左滑')
        # self.driver.swipe(x*0.9, y*0.5, x*0.1, y*0.5)

    def swipe_to_right(self):
        '''右滑

        '''
        window_size = self.get_size()
        width = window_size.get("width")
        height = window_size.get("height")
        try:
            self.driver.swipe(width*0.1, height*0.5, width*0.9, height*0.5)
            time.sleep(0.5)
        except Exception:
            self.save_screenshot('无法右滑')

    def swipe_to_up(self):
        '''上滑

        '''
        window_size = self.get_size()
        width = window_size.get("width")
        height = window_size.get("height")
        try:
            self.driver.swipe(width*0.5, height*0.9, width*0.5, height*0.1)
            time.sleep(0.5)
        except Exception:
            self.save_screenshot('无法上滑')

    def swipe_to_down(self):
        '''下滑、下拉刷新

        '''
        window_size = self.get_size()
        width = window_size.get("width")
        height = window_size.get("height")
        try:
            self.driver.swipe(width*0.5, height*0.4, width*0.5, height*0.9)
            time.sleep(1)
        except Exception:
            self.save_screenshot('无法下滑、下拉刷新')

    def location_slide(self,start_x,start_y,end_x,end_y,duration=None):
        # 根据相对坐标滑动，start_x：起始横坐标，start_y：起始纵坐标，end_x：结束时横坐标，end_y：结束时纵坐标，duration：滑动持续时间，单位毫秒，默认None（一般设置500-1000毫秒 0.5-1秒比较合适）
        window_size = self.get_size()
        width = window_size.get("width")
        height = window_size.get("height")
        self.driver.swipe(start_x / 1080 * width, start_y / 2211 * height, end_x / 1080 * width,end_y / 2211 * height)

    def scroll_here_to_there(self,a,b):
        # 根据元素位置滑动，从a滑动到b
        self.driver.scroll(a,b)





    def save_screenshot(self, describe):     # describe 截图名称
        self.logger.debug("BasePage.save_screenshot(%s)", describe)
        if not os.path.exists(SCREENSHOT_DIR):  # 判断目录是否存在
            self.logger.debug("if not os.path.exists(%s):", SCREENSHOT_DIR)
            os.mkdir(SCREENSHOT_DIR)    # 以数字权限模式创建目录
            self.logger.debug("os.mkdir(%s)", SCREENSHOT_DIR)
        file_name = SCREENSHOT_DIR + "\\{}_{}.png".format(datetime.strftime(datetime.now(),"%Y-%m-%d--%H-%M-%S"), describe)
        self.driver.save_screenshot(file_name)
        with open(file_name, mode='rb') as f:
            file = f.read()
        # allure.attach(file, describe, allure.attachment_type.PNG)
        self.logger.info("进行截图！截图文件保存在：{}".format(file_name))




    def wait_second(self,status,second):
        self.logger.debug("BasePage.wait_second(%s,%s)", status,second)
        if status == 1:  #如果status等于1，代表强制等待,second 代表等待时长，单位为秒
            self.logger.debug("time.sleep(%s)", second)
            time.sleep(second)
        if status == 2:  #如果status等于2，代表隐式等待,second 代表等待时长，单位为秒
            self.logger.debug("self.driver.implicitly_wait(%s)", second)
            self.driver.implicitly_wait(second)

    def quit(self):
        self.logger.debug("BasePage.quit")
        self.logger.debug("self.driver.quit()")
        self.driver.quit()