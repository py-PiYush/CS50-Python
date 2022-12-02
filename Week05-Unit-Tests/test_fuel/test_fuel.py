from fuel import convert, gauge
import pytest


def test_fraction():
    assert gauge(convert("4/5")) == "80%"
    assert gauge(convert("1/2")) == "50%"


def test_less_than_one():
    assert gauge(convert("9/1000")) == "E"
    assert gauge(convert("4/1000")) == "E"


def test_more_than_99():
    assert gauge(convert("99/100")) == "F"


def test_exceptions():
    with pytest.raises(ValueError):
        convert("cat/dog")
    with pytest.raises(ZeroDivisionError):
        convert("-1/0")
