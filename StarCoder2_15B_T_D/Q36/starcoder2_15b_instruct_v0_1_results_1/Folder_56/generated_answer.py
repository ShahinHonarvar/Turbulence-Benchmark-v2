def filter_chars(s):
    result = []
    for c in s:
        if c < '/' or c >= 'J':
            result.append(c)
    return ''.join(result)