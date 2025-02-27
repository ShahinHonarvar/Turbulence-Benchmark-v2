def filter_chars(s):
    result = []
    for c in s:
        if c < 'F' or c > 'n':
            result.append(c)
    return ''.join(result)