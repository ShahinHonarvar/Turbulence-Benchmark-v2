def filter_chars(s: str) -> str:
    filtered = ''
    for c in s:
        if c < '&' or c > 'v':
            filtered += c
    return filtered