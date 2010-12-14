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

<table border="1"cellpadding="2" cellspacing="0" width="800">
  <tr>
    <th> Test </th>
    <th> CTest </th>
    <th> Description </th>
    <th> Instructions </th>
    <th> Expected Results/Comments </th>
  </tr>

<tr>
  <td> Echo </td>
  <td> YES </td>
  <td> Test echo in a dg-shell </td>
  <td> cd _build <br> make test </td>
  <td> Passed </td>
</tr>

<tr>
  <td> Coshell </td>
  <td> YES </td>
  <td> Test coshell </td>
  <td> cd _build <br> make test </td>
  <td> Passed </td>
</tr>

<tr>
  <td> Simu </td>
  <td> YES </td>
  <td> Test left-hand task on robosimu </td>
  <td> cd _build <br> make test </td>
  <td> Passed </td>
</tr>

<tr>
  <td> Simu-viz </td>
  <td> NO </td>
  <td> Test left-hand task on robosimu <br> with vizualization</td>
  <td> sot-gui2.py -o <br> dg-shell scripts/left-hand-simu.sot <br>
  click Simulate in sot-gui2.py </td>
  <td> Robot moves its right hand while keeping the right foot in place. </td>
</tr>

<tr>
  <td> SoT-OpenHRP 1</td>
  <td> NO </td>
  <td> Test SoT entity in OpenHRP</td>
  <td> Open OpenHRP with HRP2JRLBush.xml
    <br>  $OPENHRPHOME/bin/unix/OpenHRPpy
    scripts-openhrp/sot_minimal.py
    <br> Open sot-gui2.py, click Refresh.
  </td>
  <td width="300">
 Two entities appear in the graph: <i>coshell</i> and <i>OpenHRP</i>. <br>
 <i>OpenHRP.state</i> should be  updated at a decent rate.
  </td>
</tr>
<tr>
  <td> SoT-OpenHRP 2 </td>
  <td> NO </td>
  <td> Test left-hand task in OpenHRP</td>
  <td> Open OpenHRP with HRP2JRLBush.xml
    <br>  $OPENHRPHOME/bin/unix/OpenHRPpy scripts-openhrp/sot_minimal.py
    <br> dg-coshell
    <br> in dg-coshell: $SOT-TESTS-ROOT/scripts-sot/left-hand-hrp2_14.sot
  </td>
  <td width="300"> HRP2 moves its right hand while keeping
    the right foot in  place. <br>
    The left foot slides slightly
    since no constraints is imposed on it.
</td>
</tr>

<tr>
  <td> </td>
  <td> </td>
  <td> </td>
  <td> </td>
  <td> </td>
</tr>

</table>
