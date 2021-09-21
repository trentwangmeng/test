from Utils.tool_log import logger
import logging
class test(object):
    def testsss(self):
        log = logger()
        contacts_name ="222"
        contacts_status = "333"
        # log.info('用户：%s' % contacts_name),log.info('状态：%s' % contacts_status)

        _logger_level = {
            'debug': logging.DEBUG,
            'info': logging.INFO,
            'warning': logging.WARNING,
            'error': logging.ERROR,
            'critical': logging.CRITICAL
        }
        a = _logger_level.get('info','debug1')
        log.info('用户：%s' % contacts_name),log.info('状态：%s' % contacts_status)
        log.info("%s%s",contacts_name, contacts_status)
        log.info('%s当前有%s个作品', contacts_name, contacts_status)
        log.info('%s的作品数量没有变化'%contacts_name)
        log.debug("toast_loc = (By.XPATH, './/*[contains(@text,'%s')]')", "ssssssasdfasdf")
aa = test()
aa.testsss()