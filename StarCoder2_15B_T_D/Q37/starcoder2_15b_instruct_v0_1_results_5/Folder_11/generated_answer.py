def filter_chars(s: str) -> str:
    filtered_chars = []
    for c in s:
        if c >= '-' and c <= 'n' or (c < '-' or c > 'n'):
            filtered_chars.append(c)
    return ''.join(filtered_chars)