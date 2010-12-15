ENABLE_TESTING()
ADD_TEST(TestEcho ${CMAKE_SOURCE_DIR}/tests/basictest.py test-echo.sot echo.txt)

ADD_TEST(TestCoshell ${CMAKE_SOURCE_DIR}/tests/basictest.py test-coshell.sot coshell.txt)

ADD_TEST(TestLeftHand ${CMAKE_SOURCE_DIR}/tests/basictest.py test-left-hand.sot left-hand.txt)
