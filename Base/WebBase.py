import time
import math
import operator

from PIL import Image
from functools import reduce
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Utils.YamlMethod import XiaoMaUtils
from Base.InitDriver import init_driver

class Base(object):
    def __init__(self, phone_name):





        self.driver = init_driver(phone_name)
        self.window_size = self.driver.get_window_size()

    def find_element_o(self, loc, timeout=30, poll=0.5):
        """
        根据定位获取单个元素

        :param loc: 元素的表达形式, 以元祖形式传递, eg. (By.ID,ID属性值)
        :param timeout: 等待时长
        :param poll: 查询频率
        :return: 定位对象
        """
        return WebDriverWait(self.driver, timeout, poll).until(lambda x: x.find_element(*loc))

    def find_elements_o(self, loc, timeout=20, poll=0.5):
        """
        根据定位获取一组元素

        :param loc: 元素的表达形式, 以元祖形式传递, eg. (By.ID,ID属性值)
        :param timeout: 等待时长
        :param poll: 查询频率
        :return: 一组定位对象
        """
        return WebDriverWait(self.driver, timeout, poll).until(lambda x: x.find_element(*loc))

    def click_element(self, loc):
        """
        点击操作

        :param loc: 元素的表达形式, 以元祖形式传递, eg. (By.ID,ID属性值)
        :return: None
        """
        self.find_element_o(loc).click()

    def long_press_element(self, ele, duration=2000):
        """
        长按操作

        :param ele: 要长按的对象
        :param duration: 长按时长, 默认为2000ms
        :return: None
        """
        TouchAction(self.driver).long_press(el=ele, duration=duration)

    def get_ele_text(self, ele):
        """
        获取元素的文本值

        :param ele: 元素对象
        :return: str
        """
        return self.get_element_attribute(ele, 'text')

    def get_ele_bounds(self, ele):
        """
        获取元素的边界

        :param ele: 元素对象
        :return: str, 形式如: [x1,y1][x2,y2]
        """
        return self.get_element_attribute(ele, 'bounds')

    def input_text(self, loc, text):
        """
        输入操作

        :param loc: 元素的表达形式, 以元祖形式传递, eg. (By.ID,ID属性值)
        :param text: 输入的内容
        :return:
        """
        ele = self.find_element_o(loc)
        ele.clear()
        ele.send_keys(text)

    def is_display(self, loc):
        """
        判断元素是否存在, 存在返回True, 不存在返回False

        :param loc: 元素的表达形式, 以元祖形式传递, eg. (By.ID,ID属性值)
        :return: bool
        """

        try:
            self.find_element_o(loc, timeout=10)
            return True
        except Exception as e:
            return False


    def getSize(self):
        resolution = self.driver.get_window_size()  # 获取手机分辨率
        resolution_width = resolution.get('width')   # 赋值手机分辨率-宽
        resolution_height = resolution.get('height') # 赋值手机分辨率-高
        return (resolution_width, resolution_height)

    # 根据相对坐标滑动，start_x：起始横坐标，start_y：起始纵坐标，end_x：结束时横坐标，end_y：结束时纵坐标，duration：滑动持续时间，单位毫秒，默认None（一般设置500-1000毫秒 0.5-1秒比较合适）
    def location_slide(self,start_x,start_y,end_x,end_y,duration=None):
        self.driver.swipe(start_x / 1080 * self.getSize()[0], start_y / 2211 * self.getSize()[1], end_x / 1080 * self.getSize()[0],end_y / 2211 * self.getSize()[1])


    def swipe_o(self, ele=None, location=None, direction='right', times=1):
        """
        根据用户输入的方向和次数, 滑动屏幕
        :param ele: 需要滑动区域的元素
        :param location: 需滑动的位置, 元组形式, eg. (x1, x2, y1, y2)
        :param direction: 滑动方向, 可选参数['up', 'down', 'left', 'right']
        :param times: 滑动次数
        :return: None
        """

        # 根据传入的元素解析滑动区域
        if ele:
            x1, y1, x2, y2 = XiaoMaUtils.convert_bounds_to_location(self.get_ele_bounds(ele))
        # 根据传入的坐标值解析滑动区域
        elif location:
            x1, x2, y1, y2 = location
        # 根据屏幕解析滑动区域
        else:
            width = self.window_size['width']
            length = self.window_size['height']
            x1 = width * 0.25
            x2 = width * 0.75
            y1 = length * 0.25
            y2 = length * 0.75

        # 循环滑动
        for i in range(times):
            if direction == 'up':
                self.driver.swipe(x1, y2, x1, y1)
            if direction == 'down':
                self.driver.swipe(x1, y1, x1, y2)
            if direction == 'right':
                self.driver.swipe(x1, y1, x2, y1)
            if direction == 'left':
                self.driver.swipe(x2, y1, x1, y1)
        time.sleep(2)

    def wait_activity_o(self, activity, timeout=10, interval=1):
        """
        等待activity加载完成

        :param activity: activity名称
        :param timeout: 等待时长
        :param interval: 循环查询时间, 默认每1s查询一次
        :return:
        """
        self.driver.wait_activity(activity, timeout, interval)

    def get_element_attribute(self, ele, attribute):
        """
        获取元素属性

        :param ele: 元素对象
        :param attribute: 属性名称
        :return: 元素属性值
        """
        if attribute == 'size':
            return ele.size
        else:
            return ele.get_attribute(attribute)

    def screenshot_part(self, element, img_name, bounds=None):
        """
            功能: 截图指定元素
            参数:
                :param element: 要获取的元素
                :param img_name: 要保存的名字
                :param bounds: 元素边界(对于无法定位到的元素, 可直接使用边界定位)
        """
        time.sleep(2)

        # 截取屏幕, 并打开该图像
        XiaoMaUtils.get_screencap()
        img = Image.open('Image/screen.png')

        if bounds:
            (x1, y1, x2, y2) = bounds
        else:
            # 获取待截取的元素的边界
            x1 = int(XiaoMaUtils.convert_bounds_to_location(self.get_element_attribute(element, 'bounds'))[0])
            y1 = int(XiaoMaUtils.convert_bounds_to_location(self.get_element_attribute(element, 'bounds'))[1])
            x2 = int(XiaoMaUtils.convert_bounds_to_location(self.get_element_attribute(element, 'bounds'))[2])
            y2 = int(XiaoMaUtils.convert_bounds_to_location(self.get_element_attribute(element, 'bounds'))[3])

        # 设置图像裁剪区域 (x左上，y左上，x右下,y右下)
        box1 = (x1, y1, x2, y2)

        # 图像裁剪
        image1 = img.crop(box1)

        # 存储裁剪得到的图像
        image1.save("Image/" + img_name + ".png")

    @staticmethod
    def image_contrast(img1="img1.png", img2="img2.png"):
        """
            功能: 比较两张图片的差异
            返回: 0.0表示是完全一致的图片, 数值越大, 图片的差异越大
        """
        image1 = Image.open("Image/" + img1)
        image2 = Image.open("Image/" + img2)

        h1 = image1.histogram()
        h2 = image2.histogram()

        result = math.sqrt(reduce(operator.add, list(map(lambda a, b: (a - b) ** 2, h1, h2))) / len(h1))

        return result



