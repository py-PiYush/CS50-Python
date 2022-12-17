import pytest
from working import convert


def test_correct():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("9:45 PM to 6:36 AM") == "21:45 to 06:36"
    assert convert("10 PM to 8 AM") == "22:00 to 08:00"


def test_incorrect_fmt():
    with pytest.raises(ValueError):
        convert("9 AM - 5 PM")
    with pytest.raises(ValueError):
        convert("9:00 AM - 5:00 PM")
    with pytest.raises(ValueError):
        convert("9 AM 5 PM")
    with pytest.raises(ValueError):
        convert("9:00 AM5:00 PM")
    with pytest.raises(ValueError):
        convert("9 to 5")


def test_incorrect_range():
    with pytest.raises(ValueError):
        convert("9 AM to 13 PM")
    with pytest.raises(ValueError):
        convert("9:45 AM to 5:68 PM")
