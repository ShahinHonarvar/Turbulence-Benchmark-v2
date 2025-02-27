def filter_chars(s):
    result = []
    for i, c in enumerate(s, 1):
        if 2 <= i <= 6 and '?' <= c <= 'f':
            continue
        result.append(c)
    return ''.join(result)