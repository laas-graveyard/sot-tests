# Copyright (C) 2010 François Bleibel, Thomas Moulard, JRL, CNRS/AIST.
#
# This file is part of sot-openhrp-scripts.
# sot-openhrp-scripts is free software: you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public License
# as published by the Free Software Foundation, either version 3 of
# the License, or (at your option) any later version.
#
# sot-openhrp-scripts is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# General Lesser Public License for more details.  You should have
# received a copy of the GNU Lesser General Public License along with
# sot-openhrp-scripts. If not, see <http://www.gnu.org/licenses/>.

INCLUDE(sot-scripts.cmake)

# Variables required for script generation.
SET(DYN_LIB_EXT ${CMAKE_SHARED_LIBRARY_SUFFIX})

SET(DG_SCRIPT_DIR ${CMAKE_INSTALL_PREFIX}/share/dynamic-graph/script)
SET(PLUGIN_LIST_FILENAME plugin.txt)

#FIXME: should be small but robot package is broken for now.
# Files from small robot have to be copied manually,
#       PreviewControlParameters.ini is also missing.
SET(HRP2_CONFIG_DIRECTORY ${HRP2_14_PREFIX}/share/hrp2_14)

SET(HRP2_10-SMALL_DIRECTORY ${HRP2_10_SMALL_PREFIX}/share/hrp2_10-small)
SET(HRP2_10-SMALL-OLD_DIRECTORY
  ${HRP2_10_SMALL_OLD_PREFIX}/share/hrp2_10-small-old)

# Check directories for required files.
IF(NOT EXISTS ${HRP2_CONFIG_DIRECTORY}/HRP2Specificities.xml
    OR NOT EXISTS ${HRP2_CONFIG_DIRECTORY}/HRP2LinkJointRank.xml)
    # OR NOT EXISTS ${HRP2_CONFIG_DIRECTORY}/HRP2SpecificitiesSmall.xml
    #OR NOT EXISTS ${HRP2_CONFIG_DIRECTORY}/HRP2LinkJointRankSmall.xml
    #OR NOT EXISTS ${HRP2_CONFIG_DIRECTORY}/PreviewControlParameters.ini
  MESSAGE(FATAL_ERROR "Missing files in HRP2-14 robot directory.")
ENDIF()

# Check that robot model exists.
SET(HRP2VRML_PATH
  ${OPENHRP_HOME}/Controller/IOserver/robot/${OPENHRP_ROBOT}/model)

# Watch for substitued variables in the sot scripts.
LIST(APPEND LOGGING_WATCHED_VARIABLES
  DYN_LIB_EXT
  HRP2_MODEL_DIRECTORY
  HRP2_CONFIG_DIRECTORY
  HRP2_10-SMALL_DIRECTORY
  HRP2_10-SMALL-OLD_DIRECTORY
  DG_SCRIPT_DIR
  PLUGIN_LIST_FILENAME
  TRACE_REPOSITORY
  )

#  Where is the trace repository?
#  FIXME: this is wrong. Trace output should go to a better place.
IF(WIN32)
  SET(TRACE_REPOSITORY "C:/tmp/")
ELSEIF(UNIX)
    SET(TRACE_REPOSITORY "/tmp/")
ELSE()
  MESSAGE(FATAL_ERROR "This platform is not supported.")
ENDIF()

INSTALL_GENERATED_SOT_SCRIPTS(share/dynamic-graph/script
  simu
)

