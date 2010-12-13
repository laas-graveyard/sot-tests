#! /usr/bin/env python
from basictest import run_test
import sys

def main():
    cmd = """echo "
import base
echo 1 2 3
" | dg-shell
"""
    run_test(cmd, sys.argv[1])

if __name__ == '__main__':
    main()
