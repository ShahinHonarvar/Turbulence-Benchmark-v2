def filter_chars(s: str) -> str:
    filtered = ''
    for c in s:
        if c >= '/' and c <= 'a' or (c < '/' or c > 'a'):
            filtered += c
    return filtered