ENABLE_TESTING()
ADD_TEST(TestEcho    ${CMAKE_SOURCE_DIR}/tests/test-echo.py    echo_result)
ADD_TEST(TestCoshell ${CMAKE_SOURCE_DIR}/tests/test-coshell.py coshell_result)
ADD_TEST(TestSimu    ${CMAKE_SOURCE_DIR}/tests/test-simu.py    simu_result)

