def filter_chars(s):
    filtered = ''
    for c in s:
        if c <= 'H' or c >= '|':
            filtered += c
    return filtered