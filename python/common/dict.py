#!/usr/bin/env python
#coding=utf-8
'''
File Name: dict.py
Author: dongjin.ydj
mail: dongjin.ydj@alibaba-inc.com
Created Time: Thu 23 Jun 2016 11:36:31 AM CST
'''
'''
python dict.py
'''

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

def dict_to_list(d, value_build_fun = lambda key, value : [key ,value]):
    res = []
    for key in d:
        res.append(value_build_fun(key, d[key]))
    return res

def load_dict(path, split_key = '\t', key_value_build_fun = lambda items : (items[0], items[1])):
    f = open(path)
    lines = f.readlines()
    f.close()
    res = {}
    for line in lines:
        line = line.strip()
        if len(line) == 0:
            continue
        items = line.split(split_key)
        key, value = key_value_build_fun(items)
        res[key] = value
    return res


def save_dict(path, dict_save, split_key = '\t', value_build_fun = lambda value : value):
    f = open(path, 'w')
    for key in dict_save:
        f.write('%s%s%s\n' % (str(key), split_key, value_build_fun(dict_save[key])))
    f.close()

if __name__ == '__main__':
    d = {'key': ['v1', 'v2', 'v3'], 'key2': ['v2', 'v3']}
    l = dict_to_list(d)
    print l
    save_dict('dict_test', d, ':', lambda value : ','.join(value))
    res = load_dict('dict_test', ':', lambda items : (items[0], items[1].split(',')))
    print res

