def filter_chars(s: str) -> str:
    filtered_chars = []
    for c in s:
        if not 38 < ord(c) < 81:
            filtered_chars.append(c)
    return ''.join(filtered_chars)