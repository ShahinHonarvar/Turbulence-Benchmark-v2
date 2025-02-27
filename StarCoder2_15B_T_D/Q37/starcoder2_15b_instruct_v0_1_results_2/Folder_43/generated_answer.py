def filter_chars(s):
    filtered = ''
    for c in s:
        if c < 'W' or c > '{':
            filtered += c
    return filtered