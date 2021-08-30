# Any pytest file should start with test_ or end with _test
# pytest method names should start with test
# Any code should be wrapped in method only
# Method name should have sense
# -k stands for method names execution
# -s logs in output
# -v stands for more info metadata
# you can run specific file with py.test <filename>
# you can mark (tag) tests @pytest.mark.smoke and then run with -m
# you can skip tests withh @pytest.mark.skip
import pytest


@pytest.mark.smoke
@pytest.mark.skip
def test_CreditCard():
    print("Hello") 


def test_greet():
    print("Good Morning")


def test_crossBrowser(crossBrowser):
    print(crossBrowser)


