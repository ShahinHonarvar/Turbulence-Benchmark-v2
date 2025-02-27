def filter_chars(s):
    filtered = ''
    for c in s:
        if c < 'F' or c > 'h':
            filtered += c
    return filtered