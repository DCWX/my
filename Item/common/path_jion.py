# -*- utf-8 -*-
#@Time    :2019/3/1222:13
#@Author  :无邪
#@File    :path_jion.py
#@Software:PyCharm

import os
class SplitPath:
    """切割路径的类"""
    def __init__(self):
        self.juepath=os.path.split(os.path.split(os.path.realpath(__file__))[0])[0]#获取当前文件路径
        # print(self.juepath)
    def  join_confname(self):
        a=os.path.join(self.juepath,"conf")
        os.path.join(a,"all.conf")
        return os.path.join(a,"all.conf")
    def  join_excelname(self):
        b=os.path.join(self.juepath,"test_case")
        os.path.join(b,"p贷接口自动化测试用例.xlsx")
        return os.path.join(b,"p贷接口自动化测试用例.xlsx")
    def join_mylogname(self):
        c=os.path.join(self.juepath,"test_result/Mlog/mylog.log")
        return c
    def join_myhtml(self):
        d= os.path.join(self.juepath, "test_result/html_report/test.html")
        return d
if __name__ == '__main__':
    split=SplitPath()
    print(split.join_confname())
    print(split.join_excelname())
    print(split.join_mylogname())
    print(split.join_myhtml())