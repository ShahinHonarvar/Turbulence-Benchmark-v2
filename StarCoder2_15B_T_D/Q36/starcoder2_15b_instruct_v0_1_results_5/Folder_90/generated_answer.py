def filter_chars(s: str) -> str:
    filtered = ''
    for c in s:
        if c < 'f' or c > '~':
            continue
        filtered += c
    return filtered