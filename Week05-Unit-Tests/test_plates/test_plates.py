from plates import is_valid


def test_num_of_char():
    assert is_valid("cs50") == True
    assert is_valid("thisiscs50") == False


def test_first_two_char():
    assert is_valid("cs50") == True
    assert is_valid("c50s") == False
    assert is_valid("($50") == False


def test_num():
    assert is_valid("cs05") == False
    assert is_valid("cs50p") == False


def test_punc():
    assert is_valid("cs50 ?") == False


def test_no_alpha():
    assert is_valid("12345") == False
    assert is_valid("$%^&") == False
