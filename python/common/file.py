#!/usr/bin/env python
#coding=utf-8
'''
File Name: file.py
Author: dongjin.ydj
mail: dongjin.ydj@alibaba-inc.com
Created Time: Thu 23 Jun 2016 11:40:41 AM CST
'''
'''
python file.py
'''

import os
import sys
import cmd
reload(sys)
sys.setdefaultencoding('utf-8')

def rm(dirPath):
    cmd_str = 'rm -r %s' % (dirPath)
    return cmd.execmd(cmd_str)

def mkdir(dirPath):
    cmd_str = 'mkdir -p %s' % (dirPath)
    return cmd.execmd(cmd_str)

def is_exist(dirPath):
    return os.path.exists(dirPath)

if __name__ == '__main__':
    print is_exist('test')
    print mkdir('test1')

