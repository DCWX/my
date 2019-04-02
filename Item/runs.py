# -*- utf-8 -*-
#@Time    :2019/3/1321:54
#@Author  :无邪
#@File    :runs.py
#@Software:PyCharm
# -*- utf-8 -*-
#@Time    :2019/3/917:35
#@Author  :无邪
#@File    :runs.py
#@Software:PyCharm
import unittest
import sys
sys.path.append("./")
print(sys.path)
import HTMLTestRunnerNew
from Item.common import test_case
from Item.common.path_jion import SplitPath
htmlname=SplitPath().join_myhtml()#报告生成路径

class Testreport:
    """导入测试用例生成测试报告"""
    def testresult(self):
        suit=unittest.TestSuite()#收集测试用例
        loader = unittest.TestLoader()  # 加载
        suit.addTest(loader.loadTestsFromModule(test_case))
        #执行用例
        with open(htmlname,"wb")as file:
            runner=HTMLTestRunnerNew.HTMLTestRunner(stream=file,
                                                    verbosity=2,
                                                    title="前程贷自动化测试报告",
                                                    description="我的第一份测试报告",
                                                    tester="无邪")
            runner.run(suit)#执行收集的用例
if __name__ == '__main__':
    Testreport().testresult()