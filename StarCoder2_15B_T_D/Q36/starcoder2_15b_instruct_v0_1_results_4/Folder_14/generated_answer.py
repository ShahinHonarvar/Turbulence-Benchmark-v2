def filter_chars(s: str) -> str:
    """
    Removes all occurrences of characters between indices 41 and 56 (both exclusive) in `s`
    that are greater than 'Z' and smaller than 'c'.
    """
    return ''.join((c for i, c in enumerate(s) if i < 41 or i >= 56 or c <= 'Z' or (c >= 'c')))