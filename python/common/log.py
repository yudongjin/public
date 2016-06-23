#!/usr/bin/env python
#coding=utf-8
'''
File Name: log.py
Author: dongjin.ydj
mail: dongjin.ydj@alibaba-inc.com
Created Time: Thu 23 Jun 2016 02:31:23 PM CST
'''
'''
python log.py
'''

import sys
import date
import public
reload(sys)
sys.setdefaultencoding('utf-8')

class LogType:
    Debug = 0
    Info = 1 
    Warn = 2
    Error = 3
    LogTypeStr = ['DEBUG', 'INFO', 'WARN', 'ERROR']

class LogFile:
    def __init__(self, handle):
        self.out = handle

    def log(self, info, log_type = LogType.Warn):
        print >> self.out, '%s [%s] %s' % (date.get_now_time(), LogType.LogTypeStr[log_type], info)

    def debug(self, info):
        self.log(info, LogType.Debug)

    def info(self, info):
        self.log(info, LogType.Info)

    def warn(self, info):
        self.log(info, LogType.Warn)

    def error(self, info):
        self.log(info, LogType.Error)

@public.singlemode
class Log:
    Debug = 0
    Info = 1
    Waring = 2
    Error = 3

    def __init__(self):
        self.log_map = {}

    def get_log(self, file_name = 'default.log'):
        if not self.log_map.has_key(file_name):
            self.log_map[file_name] = LogFile(file(file_name, 'a'))
        return self.log_map[file_name]

if __name__ == '__main__':
    Log().get_log('test.log').log('test', LogType.Info)
    Log().get_log('test.log').error('error')
    print Log().get_log('test.log') == Log().get_log('test.log')

