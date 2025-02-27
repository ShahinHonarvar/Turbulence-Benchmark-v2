def filter_chars(s: str) -> str:
    result = []
    for i, c in enumerate(s):
        if i < 13 or i >= 40:
            result.append(c)
        elif not ':' < c < 'C':
            result.append(c)
    return ''.join(result)