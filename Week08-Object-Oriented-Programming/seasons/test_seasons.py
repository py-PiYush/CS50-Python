import pytest
from seasons import get_birthday, calculate_minutes, print_words


def test_invalid_format():
    with pytest.raises(SystemExit):
        get_birthday("January 1 1990")
    with pytest.raises(SystemExit):
        get_birthday("January 1, 1990")
    with pytest.raises(SystemExit):
        get_birthday("01-01-1990")
    with pytest.raises(SystemExit):
        get_birthday("01/01/1990")
    with pytest.raises(SystemExit):
        get_birthday("Jan 01, 1990")


def test_out_of_range():
    with pytest.raises(SystemExit):
        get_birthday("1990-13-01")
    with pytest.raises(SystemExit):
        get_birthday("1990-01-34")
    with pytest.raises(SystemExit):
        get_birthday("2000-02-30")


def test_correct():
    assert (
        print_words(calculate_minutes(get_birthday("1990-01-01")))
        == "Seventeen million, three hundred thirty-six thousand, one hundred sixty minutes"
    )
