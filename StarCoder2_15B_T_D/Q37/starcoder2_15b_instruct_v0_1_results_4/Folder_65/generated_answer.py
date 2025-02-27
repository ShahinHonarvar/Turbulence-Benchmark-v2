def filter_chars(s):
    filtered = ''
    for c in s:
        if c < '0' or c > '@':
            filtered += c
    return filtered