def filter_chars(s: str) -> str:
    filtered = ''
    for c in s:
        if c < 'K' or c > 'a':
            filtered += c
    return filtered