def filter_chars(s: str) -> str:
    """
    Filters characters between indices 421 and 854 (both exclusive) in the given string `s`,
    if the character is greater than 'D' and smaller than 'J'.
    """
    filtered_chars = [c for i, c in enumerate(s) if not (421 < i < 854 and 'D' < c < 'J')]
    return ''.join(filtered_chars)