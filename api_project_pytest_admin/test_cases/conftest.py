"""
==================
Author: 严文超
2020/12/15 11:37
==================
"""
import pytest
import requests
from jsonpath import jsonpath
from common_tools.handle_config import conf

@pytest.fixture(scope="session")
def login_fixture():
    """前置方法：登录获取token"""
    # 登录接口url
    url = conf.get("environment","base_url") + "/api/login"
    # 请求数据
    params = {
        "username": conf.get("testdata","username"),
        "password": conf.get("testdata","password")
    }
    # 请求头
    headers = eval(conf.get("environment","headers"))
    # 发送请求
    response = requests.request(url=url, method='post', params=params, headers=headers).json()
    # 提取token
    token = jsonpath(response,"$..data")[0]
    # 传递参数
    yield token

@pytest.fixture()
def order_id_fixture(login_fixture):
    """前置方法：订单id获取"""
    token = login_fixture
    # 订单列表url
    url = conf.get("environment","base_url") + "/api/policyOrder/list"
    # 请求参数
    params = {
        "page": 1,
        "limit": 10,
        "insuranceIds": "201114172613844IB139855"
    }
    # 请求头
    headers = eval(conf.get("environment", "headers"))
    # 在请求头中加入token
    headers["authorization"] = token
    # 发送请求
    response = requests.request(url=url, method='GET', params=params, headers=headers)
    # 获取返回数据中第一个数据中的订单id
    order_id = response.json()["data"][0]["orderId"]
    # 传递参数
    yield token,order_id

@pytest.fixture()
def custom_id_fixture(login_fixture):
    """前置方法：线索id获取"""
    token = login_fixture
    # 线索列表url
    url = conf.get("environment", "base_url") + "/api/sysCustom/list"
    # 请求参数
    params = {
        "page": 1,
        "limit": 10,
        "checkStatusStr": 4,
        "clueTime": "2020-12-01 00:00:00,2020-12-31 23:59:59"
    }
    # 请求头
    headers = eval(conf.get("environment", "headers"))
    # 在请求头中加入token
    headers["authorization"] = token
    # 发送请求
    response = requests.request(url=url, method='GET', params=params, headers=headers)
    # 获取返回数据中第一个数据中的订单id
    custom_id = response.json()["data"][0]["customId"]
    # 传递参数
    yield token, custom_id