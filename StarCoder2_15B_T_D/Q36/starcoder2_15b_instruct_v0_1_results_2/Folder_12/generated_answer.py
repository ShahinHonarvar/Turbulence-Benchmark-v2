def filter_chars(s: str) -> str:
    filtered = ''
    for c in s:
        if c < 'm' or c >= 'w':
            filtered += c
    return filtered