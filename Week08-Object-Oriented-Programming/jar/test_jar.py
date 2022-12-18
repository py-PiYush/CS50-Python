import pytest
from jar import Jar


def test_negative_cap():
    with pytest.raises(ValueError):
        Jar(-1)
    with pytest.raises(ValueError):
        Jar(-5)


def test_correct_init():
    jar = Jar()
    assert jar.capacity == 12
    assert jar.size == 0
    assert str(jar) == ""
    jar = Jar(5)
    assert jar.capacity == 5


def test_str():
    jar = Jar(5)
    assert str(jar) == ""

    jar.deposit(3)
    assert str(jar) == "🍪🍪🍪"

    jar.withdraw(2)
    assert str(jar) == "🍪"


def test_deposit():
    jar = Jar(5)

    jar.deposit(3)
    assert jar.size == 3

    jar.deposit(1)
    assert jar.size == 4

    with pytest.raises(ValueError):
        jar.deposit(2)


def test_withdraw():
    jar = Jar(5)
    jar.deposit(4)

    jar.withdraw(1)
    assert jar.size == 3

    jar.withdraw(2)
    assert jar.size == 1

    with pytest.raises(ValueError):
        jar.withdraw(3)
