"""
==================
Author: 严文超
2020/12/8 11:09
==================
"""
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from common_tools.handle_log import log
from common_tools.handle_config import conf


class SendEmail:

    def __init__(self, user, to_addrs, pwd, host, port):
        """
        初始化邮件对象
        :param host: smtp服务器地址（qq邮箱：smtp.qq.com，163邮箱：smtp.163.com"）
        :param port: smtp服务器端口：465
        :param user: 发送方邮箱账号
        :param password: 邮箱的smtp服务授权码      "dbluuvtzsqhufajh"
        """
        self.smtplib = smtplib.SMTP_SSL(host, port)
        self.smtplib.login(user, pwd)
        self.user = user
        self.to_addrs = eval(to_addrs)

    def send_email(self, subject, content):
        """
        配置并发送邮件
        :param subject: 邮件主题
        :param content: 邮件内容
        """
        # 配置邮件内容、格式和编码格式
        message = MIMEText(content, "plain", "utf-8")
        # 添加邮件主题
        message["Subject"] = Header(subject)
        # 添加邮件发送人信息
        message["From"] = self.user
        # message["to"]只能接收字符串类型参数，需要进行转化
        message["to"] = str(self.to_addrs)
        try:
            self.smtplib.sendmail(from_addr=self.user, to_addrs=self.to_addrs, msg=message.as_string())
        except Exception as e:
            print(e)
            log.exception(e)
            raise e

        self.smtplib.quit()

# 创建邮件对象
sm = SendEmail(user=conf.get("email", "send_email"),
               to_addrs=conf.get("email", "send_to"),
               pwd=conf.get("email", "pwd"),
               host=conf.get("email", "host"),
               port=conf.getint("email", "port"))

if __name__ == '__main__':
    sm.send_email(subject=conf.get("email", "subject"),
                  content="测试邮件内容")
