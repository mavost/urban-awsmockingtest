# Pass different values to a test function, depending on command line options
# https://docs.pytest.org/en/7.1.x/example/simple.html

def test_answer(cmdopt):
    if cmdopt == "type1":
        print("first")
    elif cmdopt == "type2":
        print("second")
    assert 0  # to see what was printed - will always fail
