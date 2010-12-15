import sys
sys.path.append('@HRP2_SCRIPT_DIR@')
import time
import hrp
import hstsetup
from hrp import *
from hrp_configs import *

corba_string = "-ORBconfig../../../../../Common/orb.conf"
ms = findPluginManager("motionsys")
ms.load('seqplay')
seq = hrp.SequencePlayerHelper.narrow(
    ms.create("seqplay","seq", corba_string))
seq.start()

ms.load("StackOfTasks")
initialPositions = defaultInitialPositions
robot = Hrp2_14

corba_string = "-ORBconfig../../../../../Common/orb.conf"
robot_string = ""
if ( robot == Hrp2_10 ):
    robot_string = "HRP2JRL10Small"
SoT = ms.create("StackOfTasks","SoT",robot_string)

seq.sendMsg( ":joint-angles "
             + initialPositions[robot].rleg
             + " "
             + initialPositions[robot].lleg
             + " "
             + initialPositions[robot].chest
             + " "
             + initialPositions[robot].head
             + " "
             + initialPositions[robot].rarm
             + " "
             + initialPositions[robot].larm
             + " "
             + initialPositions[robot].rhand
             + " "
             + initialPositions[robot].lhand
             + " 2.5")
seq.waitInterpolation()

SoT.sendMsg(":init")
SoT.sendMsg(":script OpenHRP.refstate mc")
SoT.sendMsg(":script import base")
SoT.sendMsg(":script import coshell")
SoT.start()
print "Fished initialized, sleeping 600s"
time.sleep(600)
