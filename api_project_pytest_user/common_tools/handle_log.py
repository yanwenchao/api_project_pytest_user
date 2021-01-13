"""
==================
Author: 严文超
2020/12/4 17:32
==================
"""
import os
import logging
from common_tools.handle_path import LOGS_DIR,CONFIG_DIR
from logging.handlers import TimedRotatingFileHandler
from common_tools.handle_config import conf

class HandleLog():

    @staticmethod
    def create_loger():

        # 创建日志收集器并设置日志收集等级
        log = logging.getLogger("logger")
        log.setLevel(conf.get("logging","level"))

        # 创建日志输出到文件的渠道，按照时间轮转并添加到收集器
        fh = TimedRotatingFileHandler(filename=os.path.join(LOGS_DIR,"logs.log"),
                                      when="d",
                                      interval=1,
                                      backupCount=7,
                                      encoding="utf-8")
        fh.setLevel(conf.get("logging","fh_level"))
        log.addHandler(fh)

        # 创建日志输出到控制台的渠道,并添加到日志收集器
        sh = logging.StreamHandler()
        sh.setLevel(conf.get("logging","sh_level"))
        log.addHandler(sh)

        # 设置输出格式
        formatter = '%(asctime)s - [%(filename)s-->line:%(lineno)d] - %(levelname)s: %(message)s'
        mate = logging.Formatter(formatter)

        # 添加日志输出格式
        fh.setFormatter(mate)
        sh.setFormatter(mate)

        return log

log = HandleLog.create_loger()
if __name__ == '__main__':
    log.debug("用于测试的debug等级日志信息")
    log.info("用于测试的info等级日志信息")
    log.warning("用于测试的warning等级日志信息")
    log.error("用于测试的error等级日志信息")
    log.critical("用于测试的critical等级日志信息")

