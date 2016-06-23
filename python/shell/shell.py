#!/usr/bin/env python
#coding=utf-8
'''
File Name: shell.py
Author: dongjin.ydj
mail: dongjin.ydj@alibaba-inc.com
Created Time: Thu 23 Jun 2016 02:29:00 PM CST
'''
'''
python shell.py
'''

import sys
import readline
import traceback
reload(sys)
sys.setdefaultencoding('utf-8')
import common.public as public
import common.date as date
import common.log as log

class Shell:
    exit_key_list = ['q', 'quit', 'exit']
    def __init__(self, info, fun_map, out = sys.stdout, shell_log = log.Log().get_log('shell.log')):
        self.info = info
        self.fun_map = fun_map
        self.out = out
        self.shell_log = shell_log
        self.time = date.RunTime()

    def run(self):
        while True:
            line = raw_input('[%s] >> ' % str(self.info))
            self.shell_log.debug(line)
            if line in self.exit_key_list:
                print >> self.out, 'exit %s' % str(self.info)
                self.shell_log.debug('exit %s' % str(self.info))
                break
            items = line.split()
            cmd = items[0]
            if not self.fun_map.has_key(cmd):
                print >> self.out, 'cmd "%s" is undefine' % cmd
                self.shell_log.info('cmd "%s" is undefine' % cmd)
                continue
            self.time.start()
            try:
                ret, output = self.fun_map[cmd](self.info, items)
            except Exception, e:
                ret = False
                output = traceback.format_exc()
            run_time = self.time.get_run_time()
            if ret:
                res = '%s\nsuccess, used %fs' % (output, run_time)
                print >> self.out, res
                self.shell_log.info(res)
            else:
                res = '%s\nerror, used %fs' % (output, run_time)
                print >> self.out, res
                self.shell_log.error(res)

def add(info, conf):
    res = 0
    for num in conf[1:]:
        res += float(num)
    return True, str(res)

if __name__ == '__main__':
    log.Log().set_level(0)
    fun_map = {'add' : add}
    Shell('main', fun_map).run()
