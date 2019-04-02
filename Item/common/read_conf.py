# -*- utf-8 -*-
#@Time    :2019/3/915:33
#@Author  :无邪
#@File    :read_conf.py
#@Software:PyCharm

from configparser import ConfigParser
class Readconf:
    """读取配置文件类"""
    def __init__(self,confname):
        self.conf=ConfigParser()#创建对象,并将对象赋值给self.conf
        open1=self.conf.read(confname,encoding="utf-8")#打开配置文件
    def read_value(self):
        """读取http请求方法"""
        httpvalues=self.conf.get("crequest","crequests")#读取配置文件中的参数
        return httpvalues#返回参数
    def read_loglevel(self):
        """读取日志级别"""
        loglevel=self.conf.get("mlog","level")
        return loglevel
    def read_logformatter(self):
        """读取日志输出格式参数"""
        logformatter=self.conf.get("mlog","formatter")
        return logformatter
    def read_button(self):
        button=self.conf.get("testcase","button")
        return button
if __name__ == '__main__':
    r=Readconf(r"D:\pycharmstudy\Item\conf\all.conf")  #创建实例调用
    print(r.read_value())#输出返回的请求方法
    print(r.read_loglevel())#输出返回的日志级别
    print(r.read_logformatter())#输出返回的日志格式

