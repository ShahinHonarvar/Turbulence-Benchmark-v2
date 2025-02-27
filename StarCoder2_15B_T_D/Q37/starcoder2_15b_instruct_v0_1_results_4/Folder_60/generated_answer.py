def filter_chars(s: str) -> str:
    filtered = ''
    for c in s:
        if not (12 <= ord(c) <= 77 and ':' <= c <= 'L'):
            filtered += c
    return filtered