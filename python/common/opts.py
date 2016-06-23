#!/usr/bin/env python
#coding=utf-8
'''
File Name: opts.py
Author: dongjin.ydj
mail: dongjin.ydj@alibaba-inc.com
Created Time: Thu 23 Jun 2016 11:38:10 AM CST
'''
'''
python opts.py
'''

import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import getopt

class Opts:
    def __init__(self, argvs = sys.argv):
        self._name = argvs[0].split('/')[-1]
        self._args = argvs[1:]
        self._conf = [['-h', '', '<help>', False, str, False]]
        pass

    def usage(self):
        opts_c = ''
        opts = ''
        opts_infos = '\n'
        for opt_char, opt_default_value , opt_info , opt_is_value , opt_type, opt_is_exist in self._conf:
            if opt_is_exist:
                opts_c += '%s ' % opt_char
            else:
                opts += '%s ' % opt_char
            opts_infos += '%s %s\n' % (opt_char, opt_info)
        if len(opts) > 0:
            opts = '[%s]' % opts[:-1]
        return '%s %s%s%s' % (self._name, opts_c, opts, opts_infos)

    def add_opt(self, opt_char, opt_default_value = '', opt_info = '', opt_is_value = False, opt_type = str, opt_is_exist = False):
        if len(opt_char) != 1:
            print opt_char, 'not a access char . exit'
            sys.exit()
        self._conf.append(['-' + opt_char, opt_default_value, opt_info, opt_is_value, opt_type, opt_is_exist])

    def get_opts(self):
        opts_str = ''
        for opt_char, opt_default_value , opt_info , opt_is_value , opt_type, opt_is_exist in self._conf:
            if opt_is_value:
                opts_str += '%s:' % opt_char[1]
            else:
                opts_str += opt_char[1]
        ops, args = getopt.getopt(self._args, opts_str)
        opts = {}
        for op, value in ops:
            opts[op] = value
        res = []
        for opt_char, opt_default_value , opt_info , opt_is_value , opt_type, opt_is_exist in self._conf:
            if opt_char == '-h':
                if opts.has_key('-h'):
                    print self.usage()
                    sys.exit()
                continue
            if not opts.has_key(opt_char):
                if opt_is_exist:
                    print 'no input %s , %s . exit' % (opt_char, opt_info)
                    sys.exit()
                if not opt_is_value:
                    res.append(False)
                else:
                    res.append(opt_default_value)
                    print '%s no input , set %s default %s' % (opt_char, opt_info, str(opt_default_value))
                continue
            if not opt_is_value:
                res.append(True)
            else:
                try:
                    value = opt_type(opts[opt_char])
                    res.append(value)
                    print 'get %s %s' % (opt_char, str(value))
                except:
                    print 'input %s type error , %s . exit' % (opt_char, opt_type)
                    sys.exit()
        if len(res) == 1:
            res = res[0]
        return res

if __name__ == '__main__':
    t = Opts()
    t.add_opt('i', '', 'input path', True, str, True)
    print t.usage()
    input = t.get_opts()
    print input

