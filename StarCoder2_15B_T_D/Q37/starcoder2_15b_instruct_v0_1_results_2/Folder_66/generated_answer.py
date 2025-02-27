def filter_chars(s: str) -> str:
    """
    Removes all characters between indices 27 and 85, both inclusive,
    that are greater than or equal to 'c' and smaller than or equal to 'i'.
    """
    result = []
    for i, c in enumerate(s):
        if i < 27 or i > 85 or (not 'c' <= c <= 'i'):
            result.append(c)
    return ''.join(result)