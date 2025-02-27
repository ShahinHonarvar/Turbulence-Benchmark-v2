def filter_chars(s):
    result = []
    for i, c in enumerate(s):
        if i < 73 or i > 74 or (not 'U' <= c <= 'l'):
            result.append(c)
    return ''.join(result)