def filter_chars(s):
    result = ''
    for c in s:
        if c <= 'B' or c >= 'z':
            result += c
    return result