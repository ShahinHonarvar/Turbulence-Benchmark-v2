def filter_chars(s: str) -> str:
    new_chars = []
    for c in s:
        if not (69 < ord(c) < 87 and '#' < c < 'L'):
            new_chars.append(c)
    return ''.join(new_chars)