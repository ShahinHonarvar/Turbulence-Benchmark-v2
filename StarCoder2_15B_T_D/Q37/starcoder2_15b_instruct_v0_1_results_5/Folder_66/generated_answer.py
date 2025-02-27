def filter_chars(string):
    filtered = ''
    for i, c in enumerate(string):
        if i < 27 or i > 85 or (c < 'c' or c > 'i'):
            filtered += c
    return filtered