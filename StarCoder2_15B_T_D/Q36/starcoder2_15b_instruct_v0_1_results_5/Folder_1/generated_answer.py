def filter_chars(s: str) -> str:
    filtered = ''
    for c in s:
        if c <= '#' or c >= 'L':
            filtered += c
    return filtered