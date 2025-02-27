def filter_chars(s):
    result = ''
    for c in s:
        if c < 'E' or c > 'G':
            result += c
    return result