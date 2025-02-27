def filter_chars(s):
    filtered = ''
    for c in s:
        if c < 'X' or c > 'p':
            filtered += c
    return filtered