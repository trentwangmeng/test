# coding:utf-8
# ==============================
#        日志类的封装
# ==============================
import logging
from Config import config
import os

class LoggerHandler:
    """ 日志操作 """
    _logger_level = {
        'debug': logging.DEBUG,
        'info': logging.INFO,
        'warning': logging.WARNING,
        'error': logging.ERROR,
        'critical': logging.CRITICAL
    }

    def __init__(self, log_name, file_name, logger_level, stream_level='info', file_level='debug'):
        self.log_name = log_name
        self.file_name = file_name
        self.logger_level = self._logger_level.get(logger_level, 10)   # .get(a,b)字典中找不到a时，返回一个默认值b
        self.stream_level = self._logger_level.get(stream_level, 20)
        self.file_level = self._logger_level.get(file_level, 30)
        # 创建日志对象
        self.logger = logging.getLogger(self.log_name)
        #logger：日志对象，logging模块中最基础的对象，用logging.getLogger(name)方法进行初始化，name可以不填。通常logger的名字我们对应模块名
        # 设置日志级别
        self.logger.setLevel(self.logger_level)
        if not self.logger.handlers:
            # 设置日志输出流
            f_stream = logging.StreamHandler()
            f_file = logging.FileHandler(self.file_name, encoding='utf-8')
            """            
            创建StreamHandler之后，可以通过使用以下方法设置日志级别，设置格式化器Formatter，增加或删除过滤器Filter。
            ch.setLevel(logging.WARN)  # 指定日志级别，低于WARN级别的日志将被忽略
            ch.setFormatter(formatter_name)  # 设置一个格式化器formatter
            ch.addFilter(filter_name)  # 增加一个过滤器，可以增加多个
            ch.removeFilter(filter_name)  # 删除一个过滤器
            """

            #如果运行多次上述的脚本，则每一次运行的日志都会追加到example.log，如果想要不记录之前的运行日志，需要设置filemode参数：
            #logging.basicConfig(filename=‘examle.log’, level = logging.DEBUG, filemode =‘w’)

            # 设置输出流级别
            f_stream.setLevel(self.stream_level)
            f_file.setLevel(self.file_level)
            # 设置日志输出格式
            formatter_file = logging.Formatter(
                "%(asctime)s %(name)s %(pathname)s %(funcName)s %(lineno)d %(levelname)s %(thread)d %(threadName)s %(process)d %(message)s"
            )
            formatter_stream = logging.Formatter(
                "%(asctime)s %(name)s %(filename)s %(funcName)s %(lineno)d %(levelname)s %(message)s"
            )
            """
            %(levelno)s	打印日志级别的数值
            %(levelname)s	打印日志级别名称
            %(pathname)s	打印当前执行程序的路径
            %(filename)s	打印当前执行程序名称
            %(funcName)s	打印日志的当前函数
            %(lineno)d	打印日志的当前行号
            %(asctime)s	打印日志的时间
            %(thread)d	打印线程id
            %(threadName)s	打印线程名称
            %(process)d	打印进程ID
            %(message)s	打印日志信息
            """

            f_stream.setFormatter(formatter_stream)
            f_file.setFormatter(formatter_file)
            self.logger.addHandler(f_stream)
            self.logger.addHandler(f_file)

    @property
    def get_logger(self):
        return self.logger


def logger(log_name="Trent"):
    if not os.path.exists(config.LOG_FOLDER):
        os.mkdir(config.LOG_FOLDER)
    return LoggerHandler(
        log_name=log_name,
        logger_level=config.LOG_LEVEL,
        file_name=config.LOG_FILE_NAME,   # log文件名
        stream_level=config.LOG_STREAM_LEVEL,  # 屏幕输出日志的等级
        file_level=config.LOG_FILE_LEVEL    # 文件记录日志的等级
    ).get_logger


if __name__ == '__main__':
    logger().debug('aaaa')
    # logging.warning('%s before you %s','Look','leap!')   WARNING:root:Look before you leap!