def filter_chars(s: str) -> str:
    filtered_chars = []
    for c in s:
        if not (c > '7' and c < 'H'):
            filtered_chars.append(c)
    return ''.join(filtered_chars)