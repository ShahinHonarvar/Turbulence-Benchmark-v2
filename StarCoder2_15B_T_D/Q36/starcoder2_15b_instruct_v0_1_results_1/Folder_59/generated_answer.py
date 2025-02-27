def filter_chars(s: str) -> str:
    filtered = ''
    for c in s:
        if c < '?' or c >= 'k':
            filtered += c
    return filtered