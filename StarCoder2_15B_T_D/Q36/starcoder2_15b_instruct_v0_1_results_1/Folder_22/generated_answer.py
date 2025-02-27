def filter_chars(s):
    result = ''
    for i, c in enumerate(s):
        if i < 55 or i >= 84 or c <= ';' or (c >= 'z'):
            result += c
    return result