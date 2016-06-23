#!/usr/bin/env python
#coding=utf-8
'''
File Name: list.py
Author: dongjin.ydj
mail: dongjin.ydj@alibaba-inc.com
Created Time: Thu 23 Jun 2016 11:34:55 AM CST
'''
'''
python list.py
'''

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

def list_to_dict(l, key_value_build_fun = lambda item : (item[0], item[1]), value_build_fun = lambda value_old, value_new : value_new, default_value = None):
    res = {}
    for i in l:
        key, value = key_value_build_fun(i) 
        if not res.has_key(key):
            res[key] = default_value
        res[key] = value_build_fun(res[key], value)
    return res

def load_list(path, split_key = '\t', value_build_fun = lambda items : items):
    f = open(path)
    lines = f.readlines()
    f.close()
    res = []
    for line in lines:
        line = line.strip()
        if len(line) == 0:
            continue
        items = line.split(split_key)
        res.append(value_build_fun(items))
    return res

def save_list(path, list_save, split_key = '\t', value_build_fun = lambda item : [item]):
    f = open(path, 'w')
    for item in list_save:
        f.write('%s\n' % split_key.join(value_build_fun(item)))
    f.close()

if __name__ == '__main__':
    l = [['key', ['v1', 'v2', 'v3']], ['key2', ['v2', 'v3']]]
    d = list_to_dict(l)
    print d
    save_list('list_test', l, ':', lambda value : [value[0] ,','.join(value[1])])
    res = load_list('list_test', ':', lambda items : [items[0], items[1].split(',')])
    print res
 
