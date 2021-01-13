"""
==================
Author: 严文超
2020/12/14 19:29
==================
"""

def build_message(url,error_type,request_time,response_time,status_code,response_info):
    msg = """
        接口地址：{}
        响应状态：{}
        请求时间：{}
        响应时间：{}
        响应状态码：{}     
        详细返回信息：{}
        """.format(url,error_type,request_time,response_time,status_code,response_info)
    return msg