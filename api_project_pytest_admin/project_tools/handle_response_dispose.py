"""
==================
Author: 严文超
2020/12/15 16:11
==================
"""
from project_tools.handle_buildmsg import build_message
from project_tools.handle_dingtalk import ding
from common_tools.handle_log import log


def response_dispose(response,request_time,timeout,expected,field1,field2):
    """
    响应数据处理方法
    :param response:接口响应数据
    :param request_time:接口请求时间
    :param timeout:超时时间
    :param expected:预期结果
    :param field1:要断言的字段名1（type：str）
    :param field2:要断言的字段名2（type：str）
    """
    # 将响应结果转化成json格式
    res = response.json()
    # 获取请求响应时间
    response_time = response.elapsed.total_seconds()
    # 响应内容非空，执行条件内部逻辑
    if response:
        # 响应超时，执行条件内部逻辑
        if response_time > timeout:
            # 组装并发送超时错误信息到钉钉
            ding.ding_sendmsg(build_message(url=response.url,
                                            request_time=request_time,
                                            response_time=response_time,
                                            status_code=res["code"],
                                            error_type="响应超时",
                                            response_info=response.text[0:200]))
            # 组装并收集超时错误信息到日志收集器
            log.error(build_message(url=response.url,
                                    request_time=request_time,
                                    response_time=response_time,
                                    status_code=res["code"],
                                    error_type="响应超时",
                                    response_info=response.text))
        # 断言状态码、消息信息
        try:
            assert res[field1] == expected[field1]
            assert res[field2] == expected[field2]
        # 捕获断言错误，执行内部代码
        except AssertionError as e:
            # 组装并发送断言错误信息到钉钉
            ding.ding_sendmsg(build_message(url=response.url,
                                            request_time=request_time,
                                            response_time=response_time,
                                            status_code=res["code"],
                                            error_type="断言错误：{}:{}=={}；{}:{}=={}".format(field1,res[field1],expected[field1],field2,res[field2],expected[field2]),
                                            response_info=response.text[0:200]))
            # 组装并收集断言错误信息到日志收集器
            log.error(build_message(url=response.url,
                                    request_time=request_time,
                                    response_time=response_time,
                                    status_code=res["code"],
                                    error_type="断言错误",
                                    response_info=response.text))
            log.exception(e)
            # 抛出断言异常
            raise e
        # 断言通过，用例正常执行，收集日志信息
        else:
            log.info(build_message(url=response.url,
                                   request_time=request_time,
                                   response_time=response_time,
                                   status_code=res["code"],
                                   error_type="执行通过",
                                   response_info=response.text))
    # 响应内容为空，发送消息并收集日志
    else:
        ding.ding_sendmsg(build_message(url=response.url,
                                        request_time=request_time,
                                        response_time=response_time,
                                        status_code=res["code"],
                                        error_type="响应内容为空",
                                        response_info=response.text[0:200]))
        log.error(build_message(url=response.url,
                                request_time=request_time,
                                response_time=response_time,
                                status_code=res["code"],
                                error_type="响应内容为空",
                                response_info=response.text))