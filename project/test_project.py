import pytest
from project import (
    welcome,
    instructions,
    store_score,
    get_high_scores,
    game,
    display_usages,
)


def test_welcome(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "g")
    assert welcome("Piyush") == "g"

    monkeypatch.setattr("builtins.input", lambda _: "i")
    assert welcome("Piyush") == "i"


def test_instructions():
    assert instructions() == None


def test_store_score():
    assert store_score(33, "text") == None


def test_get_high_scores():
    pass


def test_display_usages():
    assert display_usages() == None
