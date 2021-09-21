import os
import re
import time
import random
import datetime
import configparser
from sys import platform
import yaml
from ruamel.yaml import RoundTripDumper

class XiaoMaUtils(object):
    # 定义源文件夹的根路径
    # ROOT_PATH = 'D:\\codes\\python_2020\\xiaoma_ui_automation_base_357_music\\'


    @staticmethod
    def read_config(config_file):
        """读取配置文件, 返回一个元组类型"""
        config = configparser.ConfigParser()
        config.read('config/' + config_file, encoding="utf-8-sig")
        project_name = config.get('config', 'project_name')
        app_name = config.get('config', 'app_name')
        app_version = config.get('config', 'app_version')

        return project_name, app_name, app_version

    @staticmethod
    def yml_path(yml_name):
        '''
        返回配置文件的路径
        :param yml_name: 文件名
        :return:
        '''
        # os.path.realpath(__file__)   E:\pycharm\project\UiTestCode\DataProcessing\YamlProcessing.py
        # os.path.dirname(os.path.realpath(__file__))   E:\pycharm\project\UiTestCode\DataProcessing


        os_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), '..')
        if 'darwin' in platform.lower():
            path = os_path + "/Config/" + yml_name
        else:
            path = os_path + "\\Config\\" + yml_name
        return path

    @staticmethod
    def write_yaml_file(yaml_name, yaml_data):
        '''
        向yaml文件中写入数据
        :param yaml_name:文件名
        :param yaml_data:写入的数据，可以是任何的Python对象
        :return:
        '''
        yaml_path = XiaoMaUtils.yml_path(yaml_name)
        with open(yaml_path, "w", encoding="utf-8") as f:
            yaml.dump(yaml_data, f, encoding="utf-8", Dumper=yaml.RoundTripDumper)

    @staticmethod
    def update_yaml_file(yaml_name, **data):
        """
        更新yaml中字典对象的值
        :param yaml_name:
        :param data:
        :return:
        """
        data1 = XiaoMaUtils.read_yaml_file(yaml_name)
        if data1 is None:
            data1 = {}
        for key in data:
            data1[key] = data[key]
        XiaoMaUtils.write_yaml_file(yaml_name, data1)

    @staticmethod
    def read_yaml_file(yaml_name):
        """
        读取yaml文件的内容并返回
        :param yaml_name: 文件名
        :return:
        """
        yaml_path = XiaoMaUtils.yml_path(yaml_name)
        if os.path.exists(yaml_path):
            reader_yaml = open(yaml_path, 'rb')
            data_yaml = yaml.load(reader_yaml.read(), Loader=yaml.Loader)
            reader_yaml.close()
            return data_yaml
        else:
            return None


    @staticmethod
    def get_current_time():
        """获取系统当前时间, 返回字符串数据类型"""
        current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

        return current_time


    @staticmethod
    def convert_str_to_time(time_str):
        """ 把 00:00:45 这种形式的字符串转化为时间 """
        time_list = time_str.split(":")

        # 判断是否有小时位, 若有则封装为变量, 没有则封装为0
        if len(time_list) > 2:
            hour, minute, second = time_list
            res_time = datetime.time(int(hour), int(minute), int(second))
        else:
            minute, second = time_list
            res_time = datetime.time(0, int(minute), int(second))

        return res_time

    """
    去掉该方法, 使用字符串解析替换
    """

    # @staticmethod
    # def add_index_to_loc(loc, index=1, direction="left"):
    #     """
    #     在元素的表达形式中加入索引值
    #
    #     :param loc: 元素的表达形式, 以元祖形式传递, eg. (By.ID,ID属性值)
    #     :param index: 索引值, 默认取1
    #     :param direction: 查找"["的方向, 默认取left. left: 从左查找, 从右查找
    #     :return: 加入索引的元素表达形式
    #     """
    #     temp_str = loc[1]
    #
    #     # 查找元素表达式中要插入索引的位置
    #     flag_index = 0
    #     if direction == 'left':
    #         flag_index = temp_str.find('[')
    #     if direction == 'right':
    #         flag_index = temp_str.rfind('[')
    #     # 把索引插入到元素表达式中, 返回新的元素表达式
    #     left_str = temp_str[:flag_index + 1]
    #     right_str = temp_str[flag_index + 1:]
    #     full_str = left_str + str(index) + right_str
    #     new_loc = (loc[0], full_str)
    #     return new_loc

    @staticmethod
    def close_app(package_name):
        """
        关闭小马应用

        :param package_name: 应用名包名, 不带前缀'com.xiaoma.'
        :return:
        """
        command = 'adb shell am force-stop com.xiaoma.' + package_name
        os.system(command)

    @staticmethod
    def clear_data(package_name):
        """
        清理应用数据

        :param package_name: 应用名包名, 不带前缀'com.xiaoma.'
        :return:
        """
        command = 'adb shell pm clear com.xiaoma.' + package_name
        os.system(command)

    @staticmethod
    def get_random_int(start, end):
        """
        返回任意范围的整数, 包括左右边界
        :param start: 区间左边数
        :param end: 区间右边数
        :return: int
        """
        return random.randint(start, end)

    @staticmethod
    def convert_bounds_to_location(location):
        """
        把元素边界转哈成坐标, eg. '[x1,y1][x2,y1]' -> [x1,y1,x2,y2]

        :param location: 元素的边界, 字符串形式
        :return: 元素坐标点的列表
        """
        pattern = re.compile(r'\d+')  # 查找数字
        return pattern.findall(location)

    @staticmethod
    def get_screencap(png_name="screen.png"):
        os.system('adb shell screencap -p /sdcard/' + png_name)
        command = 'adb pull /sdcard/' + png_name + " " + os.getcwd() + '\\Image\\' + png_name
        os.system(command)


if __name__ == '__main__':
    # pass
    XiaoMaUtils.get_screencap(png_name="testcase12_collection_toast.png")
