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
    expected_res = open(output).read()
    print res
    if res == expected_res or res + "\n" == expected_res:
        return 0
    else:
        return 1

def run_script(script,output):
    script_str = open(script).read()
    cmd = """echo "
%s
" | dg-shell
"""%script_str
    return run_test(cmd, output)

def main():
    p = os.path.dirname(os.path.abspath(__file__))
    return run_script(os.path.join(p,sys.argv[1]),
             os.path.join(p,sys.argv[2]),)

if __name__ == '__main__':
    sys.exit(main())
