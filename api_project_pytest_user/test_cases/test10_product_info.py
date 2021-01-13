"""
==================
Author: 严文超
2020/12/16 17:40
==================
"""
import os
import time
import pytest
import requests
from common_tools.handle_path import DATA_DIR
from common_tools.handle_excel import OperationExcel
from common_tools.handle_config import conf
from project_tools.handle_response_dispose import response_dispose
from common_tools.handle_replacedata import replace_data


class TestProductInfo:
    """获取产品信息用例类"""
    # 读取获取产品信息测试用例数据
    read_file = OperationExcel(os.path.join(DATA_DIR,"data.xlsx"),"product_info")
    cases_data = read_file.read_excel()

    @pytest.mark.parametrize("case",cases_data)
    def test_product_info(self,case,login_fixture):
        """
        :param case: 测试用例数据
        :param login_fixture: 前置方法同名参数，用来传递参数
        """
        # 获取前置条件中的参数
        token = login_fixture
        url = conf.get("environment", "base_url") + case["url"]
        params = {}
        method = case["method"]
        expected = eval(case["expected"])
        timeout = float(case["timeout"])
        headers = eval(conf.get("environment", "headers"))
        headers["authorization"] = token
        request_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

        # 发起请求,获取响应结果
        response = requests.request(method=method, url=url, params=params, headers=headers)

        # 调用方法，进行返回数据处理
        response_dispose(response=response,
                         request_time=request_time,
                         timeout=timeout,
                         expected=expected,
                         field1="code",
                         field2="message")