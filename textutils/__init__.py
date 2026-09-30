def first_word(text: str) -> str:
    """Return the first whitespace-separated word of text."""
    words = text.split()
    return words[0] if words else ""
