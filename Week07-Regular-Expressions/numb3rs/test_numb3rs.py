import pytest
from numb3rs import validate


def test_invalid_notation():
    assert validate("127") == False
    assert validate("127.0.0") == False
    assert validate("cat") == False
    assert validate("255.127.127.0.1") == False


def test_range():
    assert validate("127.0.0.1") == True
    assert validate("255.255.255.255") == True
    assert validate("1.2.3.1000") == False
    assert validate("127.512.512.512") == False


def test_emptyness():
    assert validate("...") == False
    assert validate("192.168..1") == False
