def filter_chars(s: str) -> str:
    filtered_chars = []
    for c in s:
        if c >= '$' and c <= ';':
            continue
        filtered_chars.append(c)
    return ''.join(filtered_chars)