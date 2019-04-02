# -*- utf-8 -*-
#@Time    :2019/3/2122:55
#@Author  :无邪
#@File    :work_mysql.py
#@Software:PyCharm
from mysql import connector#导入库
class MysqlConnect:
    """操作数据库的类"""
    def __init__(self):
        liconnect={
            "host":"47.107.168.87",
            "user":"python",
            "password":"python666",
            "port":3306,
            "database":"future"
                  }
        # 建立一个链接
        self.con=connector.connect(**liconnect)
        #获取游标,取得数据库的操作权限
        self.cursor=self.con.cursor()
    def runmysql(self,sql,button):
        try:
              #操作数据表
              result =sql
              self.cursor.execute(result)  # 运行sql语句
              if button=="1":
                   sresult=self.cursor.fetchone() #返回的是元祖
                   return sresult
              elif button=="2":
                    sresult =self.cursor.fetchall() # 返回的是列表嵌套元祖
                    return sresult
              else:
                  return"参数错误"
        except AssertionError as e:
            print("执行出错{}".format(e))
        finally:
            self.cursor.close()  # 关闭游标
            self.con.commit()
            self.con.close()  # 关闭链接
if __name__ == '__main__':
    r=MysqlConnect()
    print(r.runmysql("select Id,MobilePhone from member where Id<=23528","2"))