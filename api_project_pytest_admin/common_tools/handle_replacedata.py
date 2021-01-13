"""
==================
Author: 严文超
2020/12/7 20:24
==================
"""
import re                                          # 导入re模块，进行正则匹配
from common_tools.handle_config import conf        # 导入配置文件解析器对象

def replace_data(data,cls):
    '''定义替换数据的方法'''
    '''
    :param data: 传入要替换的源数据
    :return: 返回替换后的数据
    '''
    # 判断要替换的源数据中是否包含##包裹的数据
    while re.search("#(.+?)#",data):
        # 从源数据中匹配出第一个##包裹的要被替换掉的数据对象
        item = re.search("#(.+?)#",data)
        # 提取需要被替换的字符串
        rep_data = item.group()
        # 要替换掉的属性名
        key = item.group(1)
        try:
            # 优先从配置文件中获取替换后的数据
            value = conf.get("testdata",key)
        except:
            # 若配置文件中没有，则从类属性中获取替换后的数据
            value = getattr(cls,key)
        # 使用替换后的数据来替换通过正则匹配出来的数据
        data = data.replace(rep_data,str(value))
    return data
