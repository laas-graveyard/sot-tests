#! /usr/bin/env python
__author__ = "Duong Dang"
__version__ = "0.1"

from subprocess import Popen, PIPE
import sys, os

def os_call(cmd):
    """
    """
    p= Popen(cmd, shell = True, stdout = PIPE)
    stdout, stderror = p.communicate()
    if stderror :
        raise Exception(stderror)
    # logger.debug("os_call: got %s for %s"%(stdout,cmd))
    return stdout

def run_test(cmd, output):
    """

    Arguments:
    - `cmd`:
    - `output`:
    """
    res = os_call(cmd)
    print res
    expected_res = open(output).read()
    if res != expected_res:
        return 1
    else:
        return 0

def run_script(script,output):
    print script
    script_str = open(script).read()
    print script_str
    cmd = """echo "
%s
" | dg-shell
"""%script_str
    run_test(cmd, output)

def main():
    p = os.path.dirname(os.path.abspath(__file__))
    print (os.path.join(p,sys.argv[1]),
             os.path.join(p,sys.argv[2]),)
    run_script(os.path.join(p,sys.argv[1]),
             os.path.join(p,sys.argv[2]),)

if __name__ == '__main__':
    main()
