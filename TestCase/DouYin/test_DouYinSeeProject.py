import pytest
import allure
from Page.DouYin.DouYinPage import DouYinLikePage
from Utils.tool_log import logger
from Base.AppBase import BasePage
from Config import config


@allure.feature("测试登录功能的类")  # 归为大类
class TestDouYinProcess():

    def setup_class(self):
        global Douyin
        Douyin = DouYinLikePage(config.device)


    def teardown_class(self):
        Douyin.base.quit()

    @allure.story("step1: 点击应用页")
    @allure.title("查看抖音")  # 用例标题
    @allure.description("查看妮妮抖音账号详情")  # 用例的描述
    @allure.severity(allure.severity_level.CRITICAL)  # 发生BUG时的严重程度
    #@pytest.mark.run(order=2)
    def test_Loggin(self):
        Douyin.Loggin()
        assert True

# DOUYIN = TestDouYinProcess()
# DOUYIN.test_Loggin()
# #
# if __name__ == '__main__':
#
