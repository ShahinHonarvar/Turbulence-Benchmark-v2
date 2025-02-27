def filter_chars(s: str) -> str:
    result = []
    for c in s:
        if c < '3' or c >= 'D':
            result.append(c)
    return ''.join(result)