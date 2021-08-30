# Any pytest file should start with test_ or end with _test
# pytest method names should start with test
import pytest


@pytest.mark.smoke
def test_firstProgram():
    msg = "Hello"
    assert msg == "Hi", "Test failed because strings do not match"


def test_SecondCreditCard():
    a = 4
    b = 6
    assert a+2 ==6, "Addition do no match"