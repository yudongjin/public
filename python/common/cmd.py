#!/usr/bin/env python
#coding=utf-8
'''
File Name: cmd.py
Author: dongjin.ydj
mail: dongjin.ydj@alibaba-inc.com
Created Time: Thu 23 Jun 2016 11:43:45 AM CST
'''
'''
python cmd.py
'''

import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import commands
import subprocess

def execmd(cmd, is_print = True, is_failed_exit = False, out = sys.stdout):
    if is_print:
        print >> out, 'Execute cmd : %s' % cmd
        retval = subprocess.Popen(cmd, shell=True, stdout = out).wait()
    else:
        retval, res = commands.getstatusoutput(cmd)
    if retval != 0:
        print >> out, 'Cmd : %s\nExecute failed = %d' % (cmd, retval)
        if is_failed_exit:
            sys.exit()
        return False
    return True

if __name__ == '__main__':
    execmd('ls', True)
