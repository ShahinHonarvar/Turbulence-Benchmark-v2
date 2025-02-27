def filter_chars(s):
    filtered = ''
    for i, c in enumerate(s):
        if i < 54 or i > 83 or c < 'j' or (c > 'v'):
            filtered += c
    return filtered