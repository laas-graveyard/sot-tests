#! /usr/bin/env python
__author__ = "Duong Dang"
__version__ = "0.1"

from subprocess import Popen, PIPE
import sys, os, time, re

re_num = re.compile(r"([-+]?(\d+(\.\d*)|\.\d+)([eE][-+]?\d+))")

def remove_numerical_zero(s, precison = 1e-10):
    matches = re_num.findall(s)
    zeros = []
    for match in matches:
        match = match[0]
        try:
            f = abs(float(match))
            if f < precison:
                zeros.append(match)
                s = s.replace(match, "0")
        except:
            continue
    return s

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
    res = os_call(cmd).strip()
    expected_res = open(output).read().strip()

    res = remove_numerical_zero(res)
    expected_res = remove_numerical_zero(expected_res)
    # print """"%s"\n"%s" """%(res,expected_res)
    print res
    if res == expected_res:
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
