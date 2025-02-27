def filter_chars(s: str) -> str:
    """
    Filters out characters between indices 23 and 89, both inclusive, that are greater than or equal to 'w' and
    smaller than or equal to '{'.
    """
    return ''.join((c for i, c in enumerate(s) if i < 23 or i > 89 or c < 'w' or (c > '{')))