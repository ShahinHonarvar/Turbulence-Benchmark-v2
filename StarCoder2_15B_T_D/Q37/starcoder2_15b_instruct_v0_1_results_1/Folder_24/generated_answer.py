def filter_chars(s: str) -> str:
    """
    Filters characters between indices 36 and 79 (inclusive) that are in the range '2' to's'.
    """
    filtered = [c for c in s if c < '2' or c > 's']
    return ''.join(filtered)