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
  <td> <ul> <li>cd _build <li> make test </ul> </td>
  <td> Passed </td>
</tr>

<tr>
  <td> Coshell </td>
  <td> YES </td>
  <td> Test coshell </td>
  <td> <ul> <li>cd _build <li> make test </ul> </td>
  <td> Passed </td>
</tr>

<tr>
  <td> Lefthand </td>
  <td> YES </td>
  <td> Test left-hand task on robosimu </td>
  <td> <ul> <li>cd _build <li> make test </ul> </td>
  <td> Passed </td>
</tr>

<tr>
  <td> Lefthand-viz </td>
  <td> NO </td>
  <td>
   Test left-hand task on robosimu with vizualization</td>
  <td>
  <ul>
  <li>sot-gui2.py -o
  <li> dg-shell scripts-sot/left-hand.sot scripts-sot/robot-simu.sot
  <li> in dg-shell: import coshell
  <li>click Simulate in sot-gui2.py
  </ul>
  </td>
  <td> Robot moves its right hand while keeping both feet in place. </td>
</tr>

<tr>
  <td> SoT-OpenHRP 1</td>
  <td> NO </td>
  <td> Test SoT entity in OpenHRP</td>
  <td width="200">
    <ul>
    <li>Open OpenHRP with HRP2JRLBush.xml
    <li>  $OPENHRPHOME/bin/unix/OpenHRPpy _build/scripts-openhrp/sot_minimal.py
    <li> Open sot-gui2.py, click Refresh.
    </ul>
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
  <td>
    <ul>
    <li> Open OpenHRP with HRP2JRLBush.xml
    <li> $OPENHRPHOME/bin/unix/OpenHRPpy _build/scripts-openhrp/sot_minimal.py
    <li> dg-coshell
    <li> in dg-coshell: scripts-sot/left-hand.sot
    <li> in dg-coshell: scripts-sot/robot-openhrp.sot
    </ul>
  </td>
  <td width="200"> HRP2 moves its right hand while keeping
    the both feet in  place.
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
