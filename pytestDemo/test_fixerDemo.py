# Any pytest file should start with test_ or end with _test
# pytest method names should start with test
import pytest


@pytest.mark.usefixtures("setup")
class TestExample:


    def test_fixtureDemo(self):
        print("I will execute setup in fixture")


    def test_fixtureDemo1(self):
        print("I will execute setup in fixture")


    def test_fixtureDemo2(self):
        print("I will execute setup in fixture")


    def test_fixtureDemo3(self):
        print("I will execute setup in fixture")
