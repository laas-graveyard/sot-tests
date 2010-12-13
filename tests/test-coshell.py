#! /usr/bin/env python

__author__ = "Duong Dang"
__version__ = "0.1"

from subprocess import Popen, PIPE

def os_call(cmd):
    """
    """
    p= Popen(cmd, shell = True, stdout = PIPE)
    stdout, stderror = p.communicate()
    if stderror :
        raise Exception(stderror)
    # logger.debug("os_call: got %s for %s"%(stdout,cmd))
    return stdout


def main():
    cmd = """echo "
import base
sleep 1
import coshell
coshell.help
" | dg-shell
"""
    print os_call(cmd)

if __name__ == '__main__':
    main()
