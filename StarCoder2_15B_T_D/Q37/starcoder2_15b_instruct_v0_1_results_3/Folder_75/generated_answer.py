def filter_chars(s: str) -> str:
    filtered = ''
    for c in s:
        if c < 'W' or c > 'x':
            filtered += c
    return filtered