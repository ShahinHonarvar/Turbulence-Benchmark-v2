def filter_chars(s):
    filtered = ''
    for c in s:
        if c < '8' or c > 'm':
            filtered += c
    return filtered