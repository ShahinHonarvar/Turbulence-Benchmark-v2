def filter_chars(s):
    result = []
    for i, c in enumerate(s):
        if i < 502 or i >= 946 or c <= 'W' or (c >= 'y'):
            result.append(c)
    return ''.join(result)