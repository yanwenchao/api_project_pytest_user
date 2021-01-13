"""
==================
Author: 严文超
2020/12/11 17:38
==================
"""
import os
import time
import pytest
import requests
from common_tools.handle_path import DATA_DIR
from common_tools.handle_replacedata import replace_data
from common_tools.handle_config import conf
from common_tools.handle_excel import OperationExcel
from project_tools.handle_response_dispose import response_dispose
from project_tools.handle_request_api import request_api

class TestLogin:
    """登录测试用例类"""
    # 读取接口对应数据表单，生成测试用例
    read_file = OperationExcel(os.path.join(DATA_DIR,"data.xlsx"),"login")
    cases_data = read_file.read_excel()

    # pytest用例数据参数化
    @pytest.mark.parametrize("case",cases_data)
    def test_login(self,case):
        """
        :param case: 用例数据
        """
        # 第一步：准备请求参数
        # 拼接生成接口请求url
        url = conf.get("environment","base_url") + case["url"]
        # 从配置文件获取请求头
        headers = eval(conf.get("environment","headers"))
        # 获取用例数据中的请求参数并替换
        case["params"] = replace_data(case["params"],TestLogin)
        params = eval(case["params"])
        # 获取接口请求方法
        method = case["method"]
        # 获取接口超时时间
        timeout = float(case["timeout"])
        # 获取预期结果
        expected = eval(case["expected"])
        # 获取发送请求时的本地时间，并进行格式化
        request_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

        # 第二步：发起请求并接收响应结果
        response = requests.request(method=method,url=url,params=params,headers=headers)

        # 第三步：调用封装的响应数据处理方法，进行数据处理
        response_dispose(response=response,
                         request_time=request_time,
                         timeout=timeout,
                         expected=expected,
                         field1="code",
                         field2="message")

        #
        # res = response.json()
        # # 获取请求响应时间
        # response_time = response.elapsed.total_seconds()
        #
        # # 响应内容非空，执行条件内部逻辑
        # if response:
        #     # 响应超时，执行条件内部逻辑
        #     if response_time > timeout:
        #         # 组装并发送超时错误信息到钉钉
        #         ding.ding_sendmsg(build_message(url=url,
        #                             request_time=request_time,
        #                             response_time=response_time,
        #                             status_code=res["code"],
        #                             error_type="响应超时",
        #                             response_info=response.text[0:200]))
        #         # 组装并收集超时错误信息到日志收集器
        #         log.error(build_message(url=url,
        #                             request_time=request_time,
        #                             response_time=response_time,
        #                             status_code=res["code"],
        #                             error_type="响应超时",
        #                             response_info=response.text))
        #     # 断言状态码、消息信息
        #     try:
        #         assert  res["code"] == expected["code"]
        #         assert  res["message"] == expected["message"]
        #     # 捕获断言错误，执行内部代码
        #     except AssertionError as a:
        #         # 组装并发送断言错误信息到钉钉
        #         ding.ding_sendmsg(build_message(url=url,
        #                             request_time=request_time,
        #                             response_time=response_time,
        #                             status_code=res["code"],
        #                             error_type=a,
        #                             response_info=response.text[0:200]))
        #         # 组装并收集断言错误信息到日志收集器
        #         log.error(build_message(url=url,
        #                             request_time=request_time,
        #                             response_time=response_time,
        #                             status_code=res["code"],
        #                             error_type=a,
        #                             response_info=response.text))
        #         # 抛出断言异常
        #         raise a
        #     # 断言通过，用例正常执行，收集日志信息
        #     else:
        #         log.info(build_message(url=url,
        #                             request_time=request_time,
        #                             response_time=response_time,
        #                             status_code=res["code"],
        #                             error_type="执行通过",
        #                             response_info=response.text))
        # # 响应内容为空，发送消息并收集日志
        # else:
        #     ding.ding_sendmsg(build_message(url=url,
        #                         request_time=request_time,
        #                         response_time=response_time,
        #                         status_code=res["code"],
        #                         error_type="响应内容为空",
        #                         response_info=response.text[0:200]))
        #     log.error(build_message(url=url,
        #                         request_time=request_time,
        #                         response_time=response_time,
        #                         status_code=res["code"],
        #                         error_type="响应内容为空",
        #                         response_info=response.text))

