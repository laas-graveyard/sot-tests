ENABLE_TESTING()

FUNCTION(GENERATE_TEST_SCRIPTS)
  MATH(EXPR END ${ARGC}-1)
  FOREACH(I RANGE 0 ${END})
    SET(SCRIPT ${ARGV${I}})
    # Generate script.
    CONFIGURE_FILE(${SCRIPT}.cmake ${CMAKE_CURRENT_BINARY_DIR}/${SCRIPT}.sot)
  ENDFOREACH(I RANGE 0 ${END})
ENDFUNCTION(GENERATE_TEST_SCRIPTS)

GENERATE_TEST_SCRIPTS(
  test-echo
  test-coshell
  test-left-hand
)

ADD_TEST(TestEcho ${CMAKE_SOURCE_DIR}/tests/basictest.py ${CMAKE_CURRENT_BINARY_DIR}/test-echo.sot ${CMAKE_SOURCE_DIR}/tests/echo.txt)
ADD_TEST(TestCoshell ${CMAKE_SOURCE_DIR}/tests/basictest.py ${CMAKE_CURRENT_BINARY_DIR}/test-coshell.sot ${CMAKE_SOURCE_DIR}/tests/coshell.txt)
ADD_TEST(TestLeftHand ${CMAKE_SOURCE_DIR}/tests/basictest.py ${CMAKE_CURRENT_BINARY_DIR}/test-left-hand.sot ${CMAKE_SOURCE_DIR}/tests/left-hand.txt)
