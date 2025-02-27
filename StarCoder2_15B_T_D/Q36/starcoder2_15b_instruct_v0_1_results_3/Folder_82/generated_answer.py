def filter_chars(s: str) -> str:
    filtered_chars = []
    for c in s:
        if c <= 'V' or c >= 'j':
            filtered_chars.append(c)
    return ''.join(filtered_chars)