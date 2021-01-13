"""
==================
Author: 严文超
2020/12/16 10:14
==================
"""
import time
import requests
from common_tools.handle_config import conf
from common_tools.handle_replacedata import replace_data
from project_tools.handle_response_dispose import response_dispose

def request_api(cls,case):
    """
    :param cls: 调用该方法的类名
    :param case: 用例数据
    """
    # 第一步：准备用例数据
    # 获取url
    url = conf.get("environment", "base_url") + case["url"]
    # 从配置文件获取请求头
    headers = eval(conf.get("environment", "headers"))
    # 获取用例数据中的请求参数并替换
    case["params"] = replace_data(case["params"], cls)
    params = eval(case["params"])
    # 获取接口请求方法
    method = case["method"]
    # 获取接口超时时间
    timeout = float(case["timeout"])
    # 获取预期结果
    expected = eval(case["expected"])
    # 获取发送请求时的本地时间，并进行格式化
    request_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

    # 第二步：发起请求并接受响应结果
    response = requests.request(method=method, url=url, params=params, headers=headers)

    # 第三步：调用响应数据处理方法，进行数据处理
    response_dispose(response=response,
                     request_time=request_time,
                     timeout=timeout,
                     expected=expected,
                     field1="code",
                     field2="message")