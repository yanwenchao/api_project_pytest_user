"""
==================
Author: 严文超
2020/12/4 15:29
==================
"""

import os
from common_tools.handle_path import CONFIG_DIR
from configparser import ConfigParser

class Config(ConfigParser):

    def __init__(self,filename,encoding = "utf-8"):
        """
        :param filename: 配置文件名
        :param encoding: 编码方式
        """
        super().__init__()
        self.filename = filename
        self.encoding = encoding
        self.read(filename,encoding)

    def write_data(self,select,option,value):
        """
        :param select: 写入的配置块
        :param option: 写入的配置项
        :param value: 配置项的值
        """
        self.set(select,option,value)
        self.write(fp=open(self.filename,"w",encoding=self.encoding))

conf = Config(os.path.join(CONFIG_DIR,"config.ini"))


