import pytest
import allure
from tools.tool_log import logger
from time import sleep
from page.guide_page import GuidePage

log = logger()

@allure.title("登录功能")  # 用例标题
@allure.feature("测试登录功能的类")  # 归为大类
class TestLogin():

    login_message = [
        {"username": "xxxxxxxxxxxx", "password": "xxxxxxxxxx"},
        {"username": "xxxxxxxxxxxx", "password": "xxxxxxxxxx"},
    ]

    @allure.story("登录用例")  # 归为子类
    @allure.severity(allure.severity_level.CRITICAL)  # 发生BUG时的严重程度
    @pytest.mark.parametrize("login_message", login_message)
    def test_login(self, common_driver, login_message):
        allure.dynamic.title("【登录用例】用户名：%s" %login_message["username"])
        allure.dynamic.description("【登录用例】用户名：%s 密码：%s" %(login_message["username"], login_message["password"]))
        guide = GuidePage(common_driver)
        with allure.step("查看向导页面"):
            loginpage = guide.check_guide()
        with allure.step("登录操作"):
            homepage = loginpage.login_action(login_message["username"], login_message["password"])
        with allure.step("检查登录状态"):
            homepage.check_login_status()

    @allure.story("登录用例")
    @allure.title("查看用户协议")  # 用例标题
    @allure.description("查看用户协议后退出")  # 用例的描述
    @allure.severity(allure.severity_level.NORMAL)
    def test_user_agreement(self, common_driver):
        guide = GuidePage(common_driver)
        with allure.step("查看向导页面"):
            loginpage = guide.check_guide()
        with allure.step("点击查看用户协议"):
            userpage = loginpage.click_user_agreement()
        with allure.step("查看用户协议"):
            userpage.view_user_agreement()
        with allure.step("检查返回是否成功"):
            loginpage.find_username_box()