sot-tests
===========

This package contains unitary tests for the sot framework.


Setup
-----

To compile this package, it is recommended to create a separate build
directory:

    mkdir _build
    cd _build
    cmake [OPTIONS] ..

Please note that CMake produces a `CMakeCache.txt` file which should
be deleted to reconfigure a package from scratch.

Usage
-----

To run various tests provided in this package:
    cd _build
    make test

To visualize with [sot-gui](https://github.com/laas/sot-gui):
    sot-gui2
    dg-shell scripts-sot/left-hand-simu.sot
    click on simulate on sot-gui
