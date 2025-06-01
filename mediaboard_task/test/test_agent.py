import pytest

from src.agent import fetch_page, get_ledger_suffix


def test_fetch_page():
    url = "https://www.google.com"
    content = fetch_page(url)
    assert isinstance(content, str)
    assert len(content) > 0
    assert (
        "<html>" in content
        or "<!DOCTYPE html>" in content
        or "<!doctype html>" in content
    )


def test_get_ledger_suffix():
    assert get_ledger_suffix(0) == "zebricky/filmy/nejlepsi/"
    assert get_ledger_suffix(1) == "zebricky/filmy/nejlepsi/?from=100"
    assert get_ledger_suffix(5) == "zebricky/filmy/nejlepsi/?from=500"
    assert get_ledger_suffix(9) == "zebricky/filmy/nejlepsi/?from=900"

    with pytest.raises(ValueError):
        get_ledger_suffix(10)
