ENABLE_TESTING()
ADD_TEST(TestEcho ${CMAKE_SOURCE_DIR}/tests/test-echo.py echo_result)
ADD_TEST(TestSimu ${CMAKE_SOURCE_DIR}/tests/test-echo.py simu_result)
