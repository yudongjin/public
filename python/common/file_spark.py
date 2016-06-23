#!/usr/bin/env python
#coding=utf-8
'''
File Name: file_spark.py
Author: dongjin.ydj
mail: dongjin.ydj@alibaba-inc.com
Created Time: Thu 23 Jun 2016 12:51:39 PM CST
'''
'''
python file_spark.py
'''

import sys
import public
from snakebite.client import Client
reload(sys)
sys.setdefaultencoding('utf-8')

def rm(dirPath):
    cmd_str = 'hdfs dfs -rm -r %s' % (dirPath)
    return cmd.execmd(cmd_str)

def is_exist(dirPath, master = public.SPARK_MASTER, port = public.SPARK_MASTER_PORT):
    client = Client(master, port, use_trash=False)
    return client.test(dirPath, exists=True, directory=True)

if __name__ == '__main__':
    print is_exist('hdfs://ydj.spark.master:9000/user')

