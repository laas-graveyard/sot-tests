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

The following table describes various tests provided in this package

+-----------+-----+--------------------------+-----------------------------------------------------------------+-----------------------------------+
|Test       |CTest|Description               |Instruction                                                      |Expected Results/Comments          |
|           |     |                          |                                                                 |                                   |
|           |     |                          |                                                                 |                                   |
+-----------+-----+--------------------------+-----------------------------------------------------------------+-----------------------------------+
|Echo       |YES  |Test echo in a dg-shell   |cd _build                                                        |Passed                             |
|           |     |                          |                                                                 |                                   |
|           |     |                          |make test                                                        |                                   |
+-----------+-----+--------------------------+-----------------------------------------------------------------+-----------------------------------+
|Coshell    |YES  |Test coshell              |cd _build                                                        |Passed                             |
|           |     |                          |                                                                 |                                   |
|           |     |                          |make test                                                        |                                   |
+-----------+-----+--------------------------+-----------------------------------------------------------------+-----------------------------------+
|Simu       |YES  |Test left-hand task with  |cd _build                                                        |Passed                             |
|           |     |robosimu                  |                                                                 |                                   |
|           |     |                          |make test                                                        |                                   |
+-----------+-----+--------------------------+-----------------------------------------------------------------+-----------------------------------+
|Simu-viz   |NO   |Test left-hand task on    |sot-gui2.py -o                                                   |Robot move right hand while keeping|
|           |     |simu with vizualization   |                                                                 |the right foot in place.           |
|           |     |                          |dg-shell scripts/left-hand-simu.sot                              |                                   |
|           |     |                          |                                                                 |                                   |
|           |     |                          |click Simulate in sot-gui2.py                                    |                                   |
+-----------+-----+--------------------------+-----------------------------------------------------------------+-----------------------------------+
|SoT-OpenHRP|NO   |Test StackOfTasks plugin  |Open OpenHRP with HRP2JRLBush.xml                                |Two entities appear in the graph:  |
|           |     |in OpenHRP                |                                                                 |coshell and OpenHRP.               |
|           |     |                          |$OPENHRPHOME/bin/unix/OpenHRPpy                                  |                                   |
|           |     |                          |scripts-openhrp/sot_minimal.py                                   |Value of OpenHRP.state should be   |
|           |     |                          |                                                                 |updated at a decent rate.          |
|           |     |                          |Open sot-gui2.py, click Refresh.                                 |                                   |
+-----------+-----+--------------------------+-----------------------------------------------------------------+-----------------------------------+
|SoT-OpenHRP|NO   |Test left-hand task in    |Open OpenHRP with HRP2JRLBush.xml                                |HRP2 move its left hand while      |
|2          |     |OpenHRP                   |                                                                 |keeping the right foot in place.   |
|           |     |                          |$OPENHRPHOME/bin/unix/OpenHRPpy scripts-openhrp/sot_minimal.py   |                                   |
|           |     |                          |                                                                 |The left foot will slide slightly  |
|           |     |                          |dg-coshell                                                       |since no constraints is imposed on |
|           |     |                          |                                                                 |it.                                |
|           |     |                          |in dg-coshell: $SOT-TESTS-ROOT/scripts-sot/left-hand-hrp2_14.sot |                                   |
|           |     |                          |                                                                 |                                   |
+-----------+-----+--------------------------+-----------------------------------------------------------------+-----------------------------------+
|           |     |                          |                                                                 |                                   |
|           |     |                          |                                                                 |                                   |
|           |     |                          |                                                                 |                                   |
+-----------+-----+--------------------------+-----------------------------------------------------------------+-----------------------------------+
|           |     |                          |                                                                 |                                   |
|           |     |                          |                                                                 |                                   |
|           |     |                          |                                                                 |                                   |
+-----------+-----+--------------------------+-----------------------------------------------------------------+-----------------------------------+
|           |     |                          |                                                                 |                                   |
|           |     |                          |                                                                 |                                   |
|           |     |                          |                                                                 |                                   |
+-----------+-----+--------------------------+-----------------------------------------------------------------+-----------------------------------+
