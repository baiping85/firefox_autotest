# -*- coding: utf-8 -*-
# @Time : 2021-04-14 15:37
# @Author : bai ping
# @QQ : 376706275
import logging
import time


class LogInfo:

    def __init__(self):
        self.logger=logging.getLogger('mike.bai')


    def set_message(self,level,msg):
        try:
            #创建时间
            now = time.strftime('%Y-%m-%d')
            #创建日志文件
            fh = logging.FileHandler('../../Log/log_'+now+'.log')
            #创建控制台输出流
            ch = logging.StreamHandler()
            #创建输出格式
            fm = logging.Formatter('%(name)s--%(asctime)s--%(levelname)s--%(message)s')
            #日志文件设置输出格式
            fh.setFormatter(fm)
            #控制端文件设置输出格式
            ch.setFormatter(fm)
            #文件对象加入logger
            self.logger.addHandler(fh)
            #控制台对象加入logger
            self.logger.addHandler(ch)
            #设置logger出入级别
            self.logger.setLevel(level=logging.DEBUG)
            #打印消息
            if level == 'debug':
                self.logger.debug(msg)
            elif level == 'info':
                self.logger.info(msg)
            elif level == 'warning':
                self.logger.warning(msg)
            elif level == 'error':
                self.logger.error(msg)
            elif level == 'critical':
                self.logger.critical(msg)
            else:
                print('level is error~')
            # # logger.info('this is info message')
            # logger.error('this is error message')
            #移除文件handle
            self.logger.removeHandler(fh)
            #移除控制台handle
            self.logger.removeHandler(ch)
        except Exception as e:
            print(e,'file operation error~')
        finally:
            #关闭文件handle
            fh.close()
            #关闭控制台handle
            ch.close()