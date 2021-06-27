"""
简单封装Log方法
"""

import os
import time
import logging.handlers

# 日志打印级别
LEVELS = {
    'debug': logging.DEBUG,
    'info': logging.INFO,
    'warning': logging.WARNING,
    'error': logging.ERROR,
    'critical': logging.CRITICAL
}

# 创建一个日志
logger = logging.getLogger()
level = 'default'


# 创建日志文件方法
def createFile(filename):
    path = filename[0:filename.rfind('/')]  # log/log1/log.py====>log/log1
    # 先判断是否有这个目录，没有就先创建目录
    # 避免后面在目录下新建文件出错
    if not os.path.isdir(path):
        os.makedirs(path)
    if not os.path.isfile(filename):
        fd = open(filename, mode='w', encoding='utf-8')
        fd.close()
    else:
        pass


# 给logger添加handler,添加内容到日志处理器中
def setHandler(levels):
    if levels == 'error':
        logger.addHandler(MyLog.errHandler)
    else:
        logger.addHandler(MyLog.handler)


# 在记录日志之后移除日志处理器
def removeHandler(levels):
    if levels == 'error':
        logger.removeHandler(MyLog.errHandler)
    else:
        logger.removeHandler(MyLog.handler)


# 获取当前时间
def getCurrentTime():
    return time.strftime(MyLog.date, time.localtime(time.time()))


# 封装框架的log模块
class MyLog:
    # 把日志输入到log目录下
    path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # D:\interAutoTest\PytestInterface
    logFile = path + '/log/log.log'
    errFile = path + '/log/error.log'
    logger.setLevel(LEVELS.get(level, logging.NOTSET))  # 设置默认值logging.NOTSET)
    createFile(logFile)
    createFile(errFile)
    date = "%Y-%m-%d  %H:%M:%S"

    #设置输出格式
    formatter = logging.Formatter(
        '[%(asctime)s]  [%(levelname)s] %(message)s', '%Y-%m-%d  %H:%M:%S'
    )
    # 创建一个handler,用于写入日志文件
    handler = logging.FileHandler(logFile, encoding='utf-8')
    errHandler = logging.FileHandler(errFile, encoding='utf-8')
    handler.setFormatter(formatter)
    errHandler.setFormatter(formatter)

    @staticmethod
    def debug(logMeg):
        setHandler('debug')
        # 文件中输出模式
        logger.debug( logMeg)
        removeHandler('debug')

    @staticmethod
    def info(logMeg):
        setHandler('info')
        logger.info( logMeg)
        removeHandler('info')

    @staticmethod
    def warning(logMeg):
        setHandler('warning')
        logger.info( logMeg)
        removeHandler('warning')

    @staticmethod
    def error(logMeg):
        setHandler('error')
        logger.error( logMeg)
        removeHandler('error')

    @staticmethod
    def critical(logMeg):
        setHandler('critical')
        logger.critical( logMeg)
        removeHandler('critical')


# 再创建一个handler,用于输出到控制台
formatter = logging.Formatter(
        '[%(asctime)s]  [%(levelname)s] %(message)s', '%Y-%m-%d  %H:%M:%S'
    )
console = logging.StreamHandler()
console.setFormatter(formatter)
logger.addHandler(console)
console.setLevel(logging.NOTSET)

if __name__ == "__main__":
    MyLog.debug('This is debug message')
    MyLog.info('This is info message')
    MyLog.warning('This is warning message')
    MyLog.error('This is error message')
    MyLog.critical('This is critical message')

