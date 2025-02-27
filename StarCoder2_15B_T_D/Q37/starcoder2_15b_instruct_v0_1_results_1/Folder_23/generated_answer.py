def filter_chars(s: str) -> str:
    """
    Removes all characters between indices 51 and 77, both inclusive,
    that are greater than or equal to 'V' and smaller than or equal to 'Y'.
    """
    filtered_chars = [c for i, c in enumerate(s) if not (51 <= i <= 77 and 'V' <= c <= 'Y')]
    return ''.join(filtered_chars)