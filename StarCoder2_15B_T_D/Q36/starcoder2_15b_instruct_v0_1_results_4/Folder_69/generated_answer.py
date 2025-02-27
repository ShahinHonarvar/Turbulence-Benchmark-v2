def filter_chars(s):
    filtered = ''
    for i, c in enumerate(s):
        if i < 343 or i >= 665 or (not '%' < c < 'U'):
            filtered += c
    return filtered