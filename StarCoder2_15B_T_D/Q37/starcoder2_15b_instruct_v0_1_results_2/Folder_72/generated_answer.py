def filter_chars(s):
    filtered = ''
    for c in s:
        if c < 'H' or c > 's':
            filtered += c
    return filtered