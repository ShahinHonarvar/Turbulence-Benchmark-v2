def filter_chars(s: str) -> str:
    filtered_chars = []
    for c in s:
        if c <= '3' or c >= 'I':
            filtered_chars.append(c)
    return ''.join(filtered_chars)