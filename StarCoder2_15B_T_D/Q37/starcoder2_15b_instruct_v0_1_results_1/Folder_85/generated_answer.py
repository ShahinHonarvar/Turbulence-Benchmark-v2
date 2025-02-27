def filter_chars(s):
    filtered = ''
    for c in s:
        if c < 'O' or c > 'd' or (c < 'O' and c > 'd'):
            filtered += c
    return filtered