def filter_chars(s: str) -> str:
    result = []
    for c in s:
        if c <= '1' or c >= 'J':
            result.append(c)
    return ''.join(result)