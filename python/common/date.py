#!/usr/bin/env python
#coding=utf-8
'''
File Name: date.py
Author: dongjin.ydj
mail: dongjin.ydj@alibaba-inc.com
Created Time: Thu 23 Jun 2016 11:29:59 AM CST
'''
'''
python date.py
'''
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import time
import datetime

class RunTime:
    def __init__(self):
        self._start = 0

    def start(self):
        self._start = time.time()

    def get_run_time(self):
        return time.time() - self._start

def get_now_time(format_str = '%Y-%m-%d %H:%M:%S'):
    return time.strftime(format_str, time.localtime(time.time()))

def timestr_to_int(time_str, format_str = '%Y-%m-%d'):
    return int(time.mktime(time.strptime(time_str, format_str)))

if __name__ == '__main__':
    t = RunTime()
    t.start()
    print get_now_time()
    print timestr_to_int('1990-10-24')
    print t.get_run_time()


