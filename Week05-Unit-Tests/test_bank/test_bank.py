from bank import value


def test_hello():
    assert value("hello") == 0
    assert value("HellO") == 0
    assert value("HELLO") == 0


def test_h_not_hello():
    assert value("hi") == 20
    assert value("HI") == 20
    assert value("Hi!!!") == 20


def test_not_h():
    assert value("What's up!") == 100
