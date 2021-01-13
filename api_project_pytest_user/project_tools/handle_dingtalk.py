"""
==================
Author: 严文超
2020/12/14 11:39
==================
"""
from project_tools.handle_buildmsg import build_message
import requests
from common_tools.handle_config import conf


class DingTalk:
    """钉钉工具"""
    def __init__(self, url):
        """初始化钉钉对象"""
        self.url = url

    def ding_sendmsg(self, msg):
        """
        发送钉钉文本消息
        :param msg: 消息内容
        """
        headers = {
            'Content-Type': 'application/json'
        }
        params = {"msgtype": "text",
                  "text": {
                      "content": msg
                  }}
        send = requests.request(url=self.url, method="post", headers=headers, json=params)
        print(send)


ding = DingTalk(conf.get("dingding","url"))
if __name__ == '__main__':
    msg = build_message(api="login",url="https://crm.o2moment.com/api/login",request_time="awq",response_time=1,status_code=200,error_message="超时错误",response="错误详细信息")
    ding.ding_sendmsg(msg)