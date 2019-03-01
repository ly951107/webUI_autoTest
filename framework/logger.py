import os.path
import logging
import os
import time

class Logger(object):
    def __init__(self,logger):#init初始化
        self.logger=logger#self当前对象
        self.logger=logging.getLogger(logger)#通过getLogger获得当前对象
        self.logger.setLevel(logging.DEBUG)#通过logger调setLevel

        #用handler写log日志
        xs=time.strftime('%Y%m%d%H%M',time.localtime((time.time())))#时间形式
        log_path=os.path.dirname(os.path.abspath('.'))+'/logs/'
        log_name=log_path+xs+'.log'
        ch=logging.StreamHandler()
        ch.setLevel(logging.INFO)

        fh=logging.FileHandler(log_name)
        fh.setLevel(logging.INFO)
        formatter = logging.Formatter('%(asctime)s-%(name)s-%(levelname)s-%(message)s')
        ch.setFormatter(formatter)
        fh.setFormatter(formatter)
        self.logger.addHandler(ch)
        self.logger.addHandler(fh)

    def getlog(self):#获取日志对象
        return self.logger
