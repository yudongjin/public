#!/usr/bin/env python
#coding=utf-8
'''
File Name: code.py
Author: dongjin.ydj
mail: dongjin.ydj@alibaba-inc.com
Created Time: Thu 23 Jun 2016 12:59:20 PM CST
'''
'''
python code.py
'''

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

def to_utf8(word):
    if type(word) != str:
        return word.encode('utf-8')
    return word

