import pytest

def test_m1():
    a = 3
    b = 4
    assert a+1 == b, "message for failing test"
    assert a != b, ""

def test_m2():
    name = 'selenium'
    assert name.upper() == 'SELENIUM'

def test_m3():
    assert True

def test_m4():
    assert True
