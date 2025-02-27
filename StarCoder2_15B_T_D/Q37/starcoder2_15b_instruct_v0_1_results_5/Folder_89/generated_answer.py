def filter_chars(text: str) -> str:
    """
    Filters out characters between indices 11 and 32, inclusive, that are in the range '!' to '@'.
    """
    filtered = [c for c in text if (c < '!' or c > '@') or c not in text[11:33]]
    return ''.join(filtered)