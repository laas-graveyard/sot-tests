#! /usr/bin/env python
from basictest import run_test
import os, sys
def main():
    script_path = os.path.join( os.path.dirname(os.path.abspath(__file__)), "..","scripts-sot")
    cmd = """echo "
run %s/left-hand-simu.sot
for i=1:1000 OpenHRP.inc
OpenHRP.state
task.error
" | dg-shell"""%script_path
    run_test(cmd, sys.argv[1])


if __name__ == '__main__':
    main()
