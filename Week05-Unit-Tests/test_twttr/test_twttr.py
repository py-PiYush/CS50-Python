from twttr import shorten


def test_lower():
    assert shorten("twitter") == "twttr"
    assert shorten("hello") == "hll"


def test_upper():
    assert shorten("TWITTER") == "TWTTR"
    assert shorten("HELLO") == "HLL"


def test_mixed():
    assert shorten("TwittEr") == "Twttr"
    assert shorten("HellO") == "Hll"
    assert shorten("fix%0") == "fx%0"


def test_sentences():
    assert shorten("How are You?") == "Hw r Y?"
