# from appium import webdriver
# from Utils.YamlMethod import XiaoMaUtils


def init_driver(self,phone_name="all"):
    """
    初始化driver

    :param use_launcher: 是否启动桌面, 默认为False, 不启动桌面, 直接启动对应应用
    :param clear_package_name: 要清除数据的应用名, 默认不清理
    :return:
    """

    # 清除应用数据
    # if clear_package_name:
    #     XiaoMaUtils.clear_data(clear_package_name)

    url = ""
    capabilities = {}
    # 设备信息
    date = XiaoMaUtils.read_yaml_file("phone.yaml")["devices"]
    for i in range(len(date)):
        if date[i]["name"] == phone_name:
            url = date[i]["url"]
            capabilities = date[i]["capabilities"]

    # 声明我们的driver对象
    driver = webdriver.Remote(url, capabilities)

    return driver
