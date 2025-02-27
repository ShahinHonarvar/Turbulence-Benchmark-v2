def filter_chars(s: str) -> str:
    keep_chars = [c for c in s if c <= 't' or c >= 'x']
    return ''.join(keep_chars)