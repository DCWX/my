import logging
from Item.common.read_conf import Readconf
from Item.common.path_jion import SplitPath
class MYLog:
    """这是一个日志收集类"""
    def __init__(self):
        self.level=Readconf(SplitPath().join_confname()).read_loglevel()
    def hander(self,level,msg):
        """设置日志输出"""
        self.mylog = logging.getLogger("mylg")  # 创建日志收集器
        self.mylog.setLevel(self.level)
        formatters=Readconf(SplitPath().join_confname()).read_logformatter()
        #方法一，配置文件中不写logging.Formatter，在当前文件创建对象
        formatter=logging.Formatter(formatters)#取到配置文件的格式后要创建实例
        # 方法二，配置文件中写入logging.Formatter，通过eval转换原类型
        # f=eval(formatters)
        #方法三，不通过配置文件，直接在当前文件写入格式
        # formatter = logging.Formatter(
        #     '%(asctime)s-%(levelname)s-%(filename)s-%(name)s-日志信息:%(message)s')
        output=logging.FileHandler(SplitPath().join_mylogname(),encoding="utf-8")
        #设置输出等级
        output.setLevel(self.level)
        #设置输出格式
        output.setFormatter(formatter)
        #输出渠道对接
        self.mylog.addHandler(output)
        if level == "DEBUG":
            self.mylog.debug(msg)
        elif level == "INFO":
            self.mylog.info(msg)
        elif level == "WARNING":
            self.mylog.warning(msg)
        elif level == "ERROR":
            self.mylog.error(msg)
        else:
            self.mylog.critical(msg)
        self.mylog.removeHandler(output)  # 清除日志渠道
    def debugs(self, msg):
            self.hander("DEBUG", msg)
    def infos(self, msg):
            self.hander("INFO", msg)
    def warning(self, msg):
            self.hander("WARNING", msg)
    def errors(self, msg):
            self.hander("ERROR", msg)
    def criticals(self, msg):
            self.hander("CRITICAL", msg)
if __name__ == '__main__':
    MYLog().debugs("shdjshfsdhfjsd")
    # print(logs)