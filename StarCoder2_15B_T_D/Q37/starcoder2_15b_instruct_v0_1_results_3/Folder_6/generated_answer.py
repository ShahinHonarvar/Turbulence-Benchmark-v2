def filter_chars(s):
    filtered = ''
    for c in s:
        if c < 'c' or c > 'n':
            filtered += c
    return filtered