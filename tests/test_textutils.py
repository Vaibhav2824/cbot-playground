from textutils import first_word


def test_first_word_returns_first_token():
    assert first_word("hello big world") == "hello"


def test_first_word_empty_string_returns_empty_string():
    assert first_word("") == ""
