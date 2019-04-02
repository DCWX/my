# -*- utf-8 -*-
#@Time    :2019/3/2122:12
#@Author  :无邪
#@File    :get_data.py
#@Software:PyCharm
import re
class GetData:
    """反射类，利用反射传送cookies"""
    cookies = None
#---------------方法1，替换---------------------
    # call="18258148330"
    # memberId="1123267"
# ---------------方法2，正则---------------------
    re_call="18258148330"
    re_pwd="wx123456"
    re_memberId="1123267"
    #上述参数也可以直接写到配置文件
def replace(t):
    """使用正则替换正常用例的手机号，密码和用户id"""
    zhengze="#(.*?)#"
    while re.search(zhengze,t):
        tel_pwd_id=re.search(zhengze,t)#在目标字符串里面根据正则表达式来查找，有匹配的字符串就返回对象
        key=tel_pwd_id.group(1)# 传参就是只返回匹配的字符串，也就是当前组的匹配字符
        # print(key)
        value=getattr(GetData,key)# 拿到我们需要去替换的值re_tel，re_pwd，re_memberId
        t=re.sub(zhengze,value,t,count=1)#替换
    return t
if __name__ == '__main__':
    r=replace('{ "mobilephone":"#re_call#","pwd":"#re_pwd#","memberId":"#re_memberId#"}')
    print(r)
# print(getattr(GetData,"cookies"))#获取cookies的值
# print(hasattr(GetData,"cookies"))#查看cookies返回结果，布尔值
# print(setattr(GetData,"cookies","jsdjsfkjsd"))#设置cookies的值
# print(delattr(GetData,"cookies"))#删除cookies的值