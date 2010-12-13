#! /usr/bin/env python

__author__ = "Duong Dang"
__version__ = "0.1"

from subprocess import Popen, PIPE
import corba_util, os

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
    script_path = os.path.join( os.path.dirname(os.path.abspath(__file__)), "..","scripts-sot")
    cmd = """echo "
run %s/left-hand-simu.sot
for i=1:1000 OpenHRP.inc
OpenHRP.state
task.error
" | dg-shell"""%script_path
    print os_call(cmd)

if __name__ == '__main__':
    main()
