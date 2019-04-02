# -*- utf-8 -*-
#@Time    :2019/3/1011:55
#@Author  :无邪
#@File    :request_http.py
#@Software:PyCharm
import requests
from Item.common.read_conf import Readconf
from Item.common.path_jion import SplitPath
http_method=Readconf(SplitPath().join_confname()).read_value()#获取配置文件中返回的请求方法
from Item.common.wlog import MYLog
#----------------------方法1：可以在这直接设置cookie传送------------------------
# url1="http://47.107.168.87:8080/futureloan/mvc/api/member/login"
# params1={"mobilephone":"18258148330","pwd":"wx123456"}
# res=requests.get(url1,params1)
# cookies=res.cookies
#--------------------------------------------------------------------------------
class HttpResquest:
    def __init__(self,urls,params):#定义传递的参数
        self.url=urls
        self.param=params
    def httprequest(self,cookies):
        if http_method=="get":#get请求，可以通过配置文件修改
            try:
                res=requests.get(self.url,self.param,cookies=cookies)#发起get请求
            except AssertionError as e:
                print("请求出错{}".format(e))
                MYLog().debugs(e)
        elif http_method=="post":#post请求，可以通过配置文件修改
            try:
                res = requests.post(self.url,self.param,cookies=cookies)
            except AssertionError as e:
                print("请求出错{}".format(e))
                MYLog().debugs(e)
        else:
            print("请求方法不正确")
            MYLog().debugs("{}请求方法不正确".format(http_method))
        return res
if __name__ == '__main__':
    a=HttpResquest("http://47.107.168.87:8080/futureloan/mvc/api/member/bidLoan",
                   {"memberId":"1123267","password":"wx123456","loanId":"10106","amount":"100000"}).httprequest()
    print(a)
