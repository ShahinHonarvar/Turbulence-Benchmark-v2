def filter_chars(s: str) -> str:
    filtered = []
    for c in s:
        if c >= '+' and c <= '}' and (not 515 <= ord(c) - ord('+') <= 538):
            filtered.append(c)
    return ''.join(filtered)