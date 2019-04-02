# -*- utf-8 -*-
#@Time    :2019/3/1012:08
#@Author  :无邪
#@File    :test_case.py
#@Software:PyCharm
import unittest
from Item.common.request_http import HttpResquest#引入http请求类
from ddt import ddt,data
from Item.common.read_excel import Readexcel#引入excel读取类
from Item.common.path_jion import SplitPath#引入路径切割类
from Item.common.wlog import MYLog#引入日志类
from Item.common.get_data import GetData#引入反射类
from Item.common.work_mysql import MysqlConnect#引入数据库操作类
from Item.common import get_data#导入正则类

#取得用例的值，传递给装饰器data
cases=Readexcel(SplitPath().join_excelname()).readcase()
# cookiess=None
#----------------------------------------------------------------------
@ddt
class TestsCases(unittest.TestCase):

    def setUp(self):
        #创建写入测试的实例
        self.w=Readexcel(SplitPath().join_excelname())
        print("-------------开始执行测试用例了------------------")
    def tearDown(self):
        print("--------------------测试结束---------------------")
    @data(*cases)
    def test_011(self,data_item):
        # global cookiess
        print("正在执行第{}条用例".format(data_item["Case_id"]))
        #-----------------------方法2：设置全局变量传送cookies------------------
        #res1 = HttpResquest(data_item["url"],eval(data_item["Params"])).httprequest(cookies=cookiess))
        # if res1.cookies:#判断cookie是否为空，不为是true
        #     cookiess=res1.cookies
        #-------------------------方法3，利用反射-------------------------------
        if data_item["sql"]!=None :
          sqls=eval(data_item["sql"])
          before_leaveamount=MysqlConnect().runmysql(sqls["sql"],"2")
          before_money=before_leaveamount[0][0]

        #------------------调用get_data模块中的替换函数（正则）替换#用例中的参数--------------------------------
        data_item["Params"]=get_data.replace(data_item["Params"])#用正则替换param里的值
        #--------------------------------------------------------------------------------
        ## 调用HttpResquest实现向服务器发起请求并传递测试用例
        res1 = HttpResquest(data_item["url"],eval(data_item["Params"])).httprequest(
            cookies=getattr(GetData, "cookies"))
        # ----------------------------------------------------------------------------
        if res1.cookies:
            setattr(GetData,"cookies",res1.cookies)
        try:
          res=res1.json()
          a=res["status"]#得到status的值
          b=res["code"]#得到code的值
          c=res["msg"]#得到msg的值
          ecpected=data_item["ExpectedResult"]#得到预期结果
          ecpect=eval(ecpected)#转成原类型(字典)
          b1=ecpect["code"]#得到code的值
          a1=ecpect["status"]#得到status的值
          c1=ecpect["msg"]#得到msg的值

          r=self.assertEqual(str(a),a1)#比较status
          r = self.assertEqual(b, b1)#比较code
          r = self.assertEqual(c, c1)#比较msg

          if  data_item["module"]=="recharge" and data_item["sql"] != None:
              #充值金额数据库查询，用充值前的账户余额加上充值的金额，判断与当前账户金额是否相等
            sqls = eval(data_item["sql"])
            after_leaveamount = MysqlConnect().runmysql(sqls["sql"], "2")
            after_money = after_leaveamount[0][0]
            qi_wang_result = before_money + int(eval(data_item["Params"])["amount"])
            r = self.assertEqual(qi_wang_result, after_money)
          elif data_item["sql"] != None and data_item["module"]=="bidLoan":
              #竞标金额数据库查询，用投资前的账户余额减去投资的金额，判断与当前账户金额是否相等
            sqls = eval(data_item["sql"])
            after_leaveamount = MysqlConnect().runmysql(sqls["sql"], "2")
            after_money = after_leaveamount[0][0]
            qi_wang_result = before_money -int(eval(data_item["Params"])["amount"])
            r = self.assertEqual(qi_wang_result, after_money)
          data_item["TestResult"]="PASS"#定义通过的用例为pass
          print("用例通过:")
          print("实际结果{}与预期结果{}一致".format(res, ecpected))
        except AssertionError as e:
            MYLog().debugs(e)#写入日志。定义最低的日志收集级别
            print("用例不通过{}".format(e))
            data_item["TestResult"] = "FAILD"#定义出错的用例为fail
            print("实际结果{}与预期结果{}不一致".format(res, ecpected))
            raise e

        finally:
            self.w.writeexcel(data_item["Case_id"]+1,10,str(res))#将实际测试结果写回
            self.w.writeexcel(data_item["Case_id"]+1,11,data_item["TestResult"])#将结果标识写回
            if data_item["sql"] != None:
                sqls = eval(data_item["sql"])
                after_leaveamount = MysqlConnect().runmysql(sqls["sql"], "2")
                after_money = after_leaveamount[0][0]
                self.w.writeexcel(data_item["Case_id"]+1,8,str(after_money))#将数据库用户最后的检查金额写回excel


if __name__ == '__main__':
    t=TestsCases()
    print(t.test_011())

