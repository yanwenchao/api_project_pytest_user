"""
==================
Author: 严文超
2020/12/15 15:11
==================
"""
import requests
import os
import pytest
import time
from common_tools.handle_config import conf
from common_tools.handle_excel import OperationExcel
from common_tools.handle_path import DATA_DIR
from project_tools.handle_response_dispose import response_dispose

class TestCustomSearch:
    """线索查询测试类"""
    # 读取excel线索查询表单测试用例数据
    read_file = OperationExcel(os.path.join(DATA_DIR,"data.xlsx"),"search_custom")
    cases_data = read_file.read_excel()

    # # pytest用例数据参数化
    @pytest.mark.parametrize("case",cases_data)
    def test_custom_search(self,case,login_fixture):
        """
        :param case: 用例数据
        :param login_fixture: 前置方法同名参数，用来进行参数传递
        """
        # 请求参数
        token = login_fixture
        url = conf.get("environment","base_url") + case["url"]
        params = eval(case["params"])
        headers = eval(conf.get("environment","headers"))
        headers["authorization"] = token
        method = case["method"]
        expected = eval(case["expected"])
        timeout = float(case["timeout"])
        # 获取发送请求时的本地时间，并格式化输出
        request_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

        # 发起请求,获取响应结果
        response = requests.request(method=method,url=url,params=params,headers=headers)

        #调用响应数据处理方法，进行数据处理
        response_dispose(response=response,
                         request_time=request_time,
                         timeout=timeout,
                         expected=expected,
                         field1="code",
                         field2="msg")

        # res = response.json()
        # # 获取请求时间
        # response_time = response.elapsed.total_seconds()
        #
        # # 响应内容非空，执行条件内部逻辑
        # if response:
        #     # 响应超时，执行条件内部逻辑
        #     if response_time > timeout:
        #         # 组装并发送超时错误信息到钉钉
        #         ding.ding_sendmsg(build_message(url=url,
        #                                         request_time=request_time,
        #                                         response_time=response_time,
        #                                         status_code=res["code"],
        #                                         error_type="响应超时",
        #                                         response_info=response.text[0:200]))
        #         # 组装并收集超时错误信息到日志收集器
        #         log.error(build_message(url=url,
        #                                 request_time=request_time,
        #                                 response_time=response_time,
        #                                 status_code=res["code"],
        #                                 error_type="响应超时",
        #                                 response_info=response.text))
        #     # 断言状态码、消息信息
        #     try:
        #         assert res["code"] == expected["code"]
        #         assert res["msg"] == expected["message"]
        #     # 捕获断言错误，执行内部代码
        #     except AssertionError as a:
        #         # 组装并发送断言错误信息到钉钉
        #         ding.ding_sendmsg(build_message(url=url,
        #                                         request_time=request_time,
        #                                         response_time=response_time,
        #                                         status_code=res["code"],
        #                                         error_type=a,
        #                                         response_info=response.text[0:200]))
        #         # 组装并收集断言错误信息到日志收集器
        #         log.error(build_message(url=url,
        #                                 request_time=request_time,
        #                                 response_time=response_time,
        #                                 status_code=res["code"],
        #                                 error_type=a,
        #                                 response_info=response.text))
        #         # 抛出断言异常
        #         raise a
        #     # 断言通过，用例正常执行，收集日志信息
        #     else:
        #         log.info(build_message(url=url,
        #                                request_time=request_time,
        #                                response_time=response_time,
        #                                status_code=res["code"],
        #                                error_type="执行通过",
        #                                response_info=response.text))
        # # 响应内容为空，发送消息并收集日志
        # else:
        #     ding.ding_sendmsg(build_message(url=url,
        #                                     request_time=request_time,
        #                                     response_time=response_time,
        #                                     status_code=res["code"],
        #                                     error_type="响应内容为空",
        #                                     response_info=response.text[0:200]))
        #     log.error(build_message(url=url,
        #                             request_time=request_time,
        #                             response_time=response_time,
        #                             status_code=res["code"],
        #                             error_type="响应内容为空",
        #                             response_info=response.text))
