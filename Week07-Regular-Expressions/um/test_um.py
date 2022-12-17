import pytest
from um import count


def test_correct():
    assert count("Regular, um, expression") == 1
    assert count("um?") == 1
    assert count("Hello, um my name is,um.... regex") == 2
    assert count("last word is um") == 1


def test_um_word():
    assert count("Umbrella is, um, dirty") == 1
    assert count("The yum toast is yummy") == 0
    assert count("Thanks for the, um, album") == 1


def test_case_insensitive():
    assert count("UM??") == 1
    assert count("Hello, Um my name is,uM.... regex") == 2
    assert count("Umbrella is, uM, dirty") == 1
