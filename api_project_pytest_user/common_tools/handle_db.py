"""
==================
Author: 严文超
2020/12/4 15:56
==================
"""
import pymysql
from common_tools.handle_config import conf

class DB():

    def __init__(self,host,port,user,password):
        """
        :param host: 数据库地址
        :param port: 数据库端口
        :param user: 用户名
        :param password: 密码
        """
        # 连接数据库
        self.con = pymysql.connect(host = host,
                                   port = port,
                                   user = user,
                                   password = password,
                                   charset = "utf8",
                                   cursorclass = pymysql.cursors.DictCursor)
        # 创建游标对象
        self.cur = self.con.cursor()

    def search_data(self,sql):
        # 提交事务，更新数据库数据
        self.con.commit()
        # 游标对象执行sql语句
        self.cur.execute(sql)
        # 获取查询到的数据
        data = self.cur.fetchall()
        return data

db = DB(host=conf.get("mysql","host"),
        port=conf.getint("mysql","port"),
        user=conf.get("mysql","user"),
        password=conf.get("mysql","password")
    )
