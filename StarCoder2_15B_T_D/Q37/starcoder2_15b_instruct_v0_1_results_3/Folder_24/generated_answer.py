def filter_chars(s):
    filtered = ''
    for c in s:
        if c < '2' or c > 's':
            filtered += c
    return filtered