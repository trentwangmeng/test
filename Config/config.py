import os
import datetime

# ---------------- 项目根目录 --------------------
BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# os.path.abspath(__file__) 作用： 获取当前脚本的完整路径  C:\Users\31542\Desktop\App_UI\Config\config.py
# os.path.dirname() 去掉文件名，返回目录 os.path.dirname(os.path.abspath(__file__))  C:\Users\31542\Desktop\App_UI\Config
# os.path.dirname(os.path.dirname(os.path.abspath(__file__)))    C:\Users\31542\Desktop\App_UI
# os.path.realpath(__file__)    作用：获取当前执行脚本的绝对路径 C:\Users\31542\Desktop\App_UI\Config\config.py

# ---------------- 隐式等待时间 --------------------
IMPLICITLY_WAIT_TIME = 5

# ---------------- 测试报告 --------------------
REPORT_PATH = os.path.join(BASE_PATH, "report")
REPORT_RESULT_PATH = os.path.join(REPORT_PATH, "allure_result")
REPORT_END_PATH = os.path.join(REPORT_PATH, "allure_report")
REPORT_HISTORY_PATH = os.path.join(REPORT_PATH, "allure_report", "history")

'''
Path1,Path2,Path3 = 'home','/develop','code'
Path10,Path20 = Path1 + Path2 + Path3,os.path.join(Path1,Path2,Path3)
print ('Path10 = ',Path10),print ('Path20 = ',Path20) 
输出   Path10 = home/developcode   Path20 = /develop\code
'''

# ---------------- 设备相关 --------------------
devices = ["RedmiDouYinWiFi","RedmiDouYinUSB"]
device = "RedmiDouYinWiFi"


# ---------------- 日志相关 --------------------
# 日志级别
LOG_LEVEL = 'debug '
LOG_STREAM_LEVEL = 'info'  # 屏幕输出流等级
LOG_FILE_LEVEL = 'debug'   # 文件输出流等级
# 日志命名
LOG_FOLDER = os.path.join(BASE_PATH, 'logs')
LOG_FILE_NAME = os.path.join(LOG_FOLDER, datetime.datetime.now().strftime('%Y-%m-%d--%H-%M-%S')+ '.log')  # python文件不支持空格和冒号

# ---------------- 邮件相关 --------------------
# 邮件文件列表
FILE_LIST = [
    os.path.join(BASE_PATH, "report", "zip", "report.zip")
]

# ---------------- 压缩文件相关 --------------------
# 要压缩文件夹的根路径
REPORT_DIR = os.path.join(BASE_PATH, "report", "allure_report")

# ---------------- bat文件相关 --------------------
ADD_REPORT_TO_GIT_FILE = os.path.join(BASE_PATH, "bat", "add_report_to_git.bat")

# ---------------- Email相关 --------------------
EMAIL_FROMADDR = '315427783@qq.com'  # 发件人邮箱
EMAIL_PASSWORD = 'iuvenxnzkywvcahe'   # 发件人授权码
EMAIL_TOADDR = [                      # 收件人地址列表
    '315427783@qq.com'
]

# ---------------- 截图相关 --------------------
SCREENSHOT_DIR = os.path.join(BASE_PATH, "ScreenShot")


