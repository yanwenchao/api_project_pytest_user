"""
==================
Author: 严文超
2020/12/17 14:21
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


class TestDeptActivityList:
    """小组活动报表用例类"""
    # 读取小组活动报表测试用例数据
    read_file = OperationExcel(os.path.join(DATA_DIR,"data.xlsx"),"dept_activity_list")
    cases_data = read_file.read_excel()

    @pytest.mark.parametrize("case",cases_data)
    def test_dept_activity_list(self,case,login_fixture):
        """
        :param case: 测试用例数据
        :param login_fixture: 前置方法同名参数，用来传递参数
        """
        # 获取参数
        token = login_fixture
        url = conf.get("environment", "base_url") + case["url"]
        case["params"] = replace_data(case["params"],TestDeptActivityList)
        params = eval(case["params"])
        method = case["method"]
        expected = eval(case["expected"])
        timeout = float(case["timeout"])
        headers = eval(conf.get("environment", "headers"))
        headers["authorization"] = token
        # 获取发送请求时的本地时间，并格式化输出
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