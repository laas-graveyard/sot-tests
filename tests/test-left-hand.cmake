run ${CMAKE_SOURCE_DIR}/scripts-sot/left-hand.sot
run ${CMAKE_SOURCE_DIR}/scripts-sot/robot-simu.sot
for i=1:1000 OpenHRP.inc
OpenHRP.state
task.error