def filter_chars(s: str) -> str:
    filtered = []
    for c in s:
        if c >= ':' and c <= 'L':
            continue
        filtered.append(c)
    return ''.join(filtered)