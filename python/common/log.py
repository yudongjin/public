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
    def __init__(self, handle, level = LogType.Warn):
        self.out = handle
        self.log_level = level

    def log(self, info, log_type = LogType.Warn):
        if log_type >= self.log_level:
            print >> self.out, '%s [%s] %s' % (date.get_now_time(), LogType.LogTypeStr[log_type], info)

    def debug(self, info):
        self.log(info, LogType.Debug)

    def info(self, info):
        self.log(info, LogType.Info)

    def warn(self, info):
        self.log(info, LogType.Warn)

    def error(self, info):
        self.log(info, LogType.Error)

    def set_level(self, level):
        self.log_level = level

@public.singlemode
class Log:
    def __init__(self):
        self.log_map = {}
        self.log_level =LogType.Warn

    def get_log(self, file_name = 'default.log'):
        if not self.log_map.has_key(file_name):
            self.log_map[file_name] = LogFile(file(file_name, 'a'), self.log_level)
        return self.log_map[file_name]

    def set_level(self, level):
        self.log_level = level
        for name in self.log_map:
            self.log_map[name].set_level(level)

if __name__ == '__main__':
    Log().get_log('test.log').log('test', LogType.Info)
    Log().set_level(LogType.Debug)
    Log().get_log('test.log').debug('error')
    print Log().get_log('test.log') == Log().get_log('test.log')

