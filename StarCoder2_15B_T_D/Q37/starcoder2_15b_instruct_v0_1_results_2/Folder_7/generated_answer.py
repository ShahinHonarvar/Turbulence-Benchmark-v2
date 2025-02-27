def filter_chars(s: str) -> str:
    """
    Filters characters between indices 521 and 722, both inclusive, and is greater than or equal to character '>' and
    smaller than or equal to character '_'.
    """
    filtered = [c for i, c in enumerate(s) if i < 521 or i > 722 or c < '>' or (c > '_')]
    return ''.join(filtered)