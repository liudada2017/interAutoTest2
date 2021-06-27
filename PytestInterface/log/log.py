# # 导入logging模块
# import logging
#
# # 创建一个日志器，就是一个logger对象
# logger = logging.getLogger("logger")
#
# # 1.设置logger日志器的日志级别为ERROR
# logger.setLevel(logging.ERROR)
#
# # 定义日志处理器File_handler
# fileHandler = logging.FileHandler("../log/test_02_log.log",encoding="utf-8")
#
# # 2.给日志处理器File_handler设置日志级别
# fileHandler.setLevel(logging.WARNING)
#
# # 给处理器传入格式器
# fileHandler.setFormatter(logging.Formatter("%(asctime)s  -  %(levelname)s  -  %(message)s"))
#
# # 定义日志处理器console_handler
# consoleHandler = logging.StreamHandler()
#
# # 3.设置处理器日志级别
# consoleHandler.setLevel(logging.DEBUG)
#
# # 给处理器传入格式器
# consoleHandler.setFormatter(logging.Formatter("%(asctime)s  -  %(levelname)s  -  %(message)s"))
#
# # 把两个处理器添加到日志器中
# logger.addHandler(fileHandler)
# logger.addHandler(consoleHandler)
#
# logger.debug("debug message")
# logger.info("info message")
# logger.warning("warning message")
# logger.error("error message")
# logger.critical("critical message")


"""
logger日志器设置的日志输出等级>handler
输出结果：
2021-05-26 11:10:23,247  -  ERROR  -  error message
2021-05-26 11:10:23,247  -  CRITICAL  -  critical message
"""


import  logging
import  logging.handlers
import  datetime

logger = logging.getLogger("logger")
logger.setLevel(logging.DEBUG)
allHander = logging.FileHandler("../log/all.log", encoding="utf-8")
allHander.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))
errorHander = logging.FileHandler("../log/error.log",encoding="utf-8")
errorHander.setLevel(logging.ERROR)
errorHander.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(filename)s[:%(lineno)d] - %(message)s"))
logger.addHandler(allHander)
logger.addHandler(errorHander)
logger.debug("debug message")
logger.info('info message')
logger.warning('warning message')
logger.error('error message')
logger.critical('critical message')


