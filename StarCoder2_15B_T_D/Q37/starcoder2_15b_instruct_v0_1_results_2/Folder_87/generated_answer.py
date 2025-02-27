def filter_chars(s: str) -> str:
    """
    Filters characters in a string `s` between indices 18 and 81 (inclusive) that are greater than or equal to 'W' and smaller than or equal to '['.
    """
    filtered = ''
    for i, c in enumerate(s):
        if (i >= 18 and i <= 81) and (c >= 'W' and c <= '['):
            continue
        filtered += c
    return filtered