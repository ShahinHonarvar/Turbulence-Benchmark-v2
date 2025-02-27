def filter_chars(s: str) -> str:
    filtered = []
    for c in s:
        if c < 'J' or c > 'b':
            filtered.append(c)
    return ''.join(filtered)