import os
import pytest
from Utils.tool_log import logger
from Utils.tool_zip import report_zip
from Utils.tool_manager import TestManager
from Utils.tool_email import send_default_email
from multiprocessing import Pool

device_infos = [
    {"platformVersion": "7.1.2", "serverPort": 4725, "deviceName": "emulator-5554"},
    #{"platformVersion": "9", "serverPort": 4727, "deviceName": "79600c9"}
]

def run_parallel(device_info):
    pytest.main([f"--cmdopt={device_info}", "--alluredir",
                 "./report/allure_result"])

def pytest_start():
    with Pool(len(device_infos)) as pool:
        pool.map(run_parallel, device_infos)
        pool.close()
        pool.join()


if __name__ == '__main__':
    log = logger()
    log.info("开始执行测试，当前APP版本:2.9.4 debug")
    mytest = TestManager()
    # mytest.del_old_result()       # 删除旧的测试结果数据
    # mytest.del_old_screenshot()   # 删除旧的测试截图
    pytest_start()                # 启动测试
    mytest.generate_report()      # 生成测试报告
    # mytest.add_report_to_git()   # 推送报告到git
    # report_zip()                 # 压缩测试报告文件
    # send_default_email()         # 发送测试报告邮件
    # mytest.run_allure_server()   # 运行allure服务
