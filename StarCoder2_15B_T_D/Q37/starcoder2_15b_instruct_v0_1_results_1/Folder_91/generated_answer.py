def filter_chars(s: str) -> str:
    filtered = ''
    for c in s:
        if not (c.isascii() and 'B' <= c <= 'H'):
            filtered += c
    return filtered