ENABLE_TESTING()
ADD_TEST(TestEcho    ${CMAKE_SOURCE_DIR}/tests/test-echo.py ${CMAKE_SOURCE_DIR}/tests/echo.txt)
ADD_TEST(TestCoshell ${CMAKE_SOURCE_DIR}/tests/test-coshell.py ${CMAKE_SOURCE_DIR}/tests/coshell.txt)
ADD_TEST(TestSimu    ${CMAKE_SOURCE_DIR}/tests/test-simu.py ${CMAKE_SOURCE_DIR}/tests/simu.txt)

