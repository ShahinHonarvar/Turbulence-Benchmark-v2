def filter_chars(s: str) -> str:
    filtered_chars = []
    for c in s:
        if not (138 <= ord(c) <= 920 and '6' <= c <= 'A'):
            filtered_chars.append(c)
    return ''.join(filtered_chars)