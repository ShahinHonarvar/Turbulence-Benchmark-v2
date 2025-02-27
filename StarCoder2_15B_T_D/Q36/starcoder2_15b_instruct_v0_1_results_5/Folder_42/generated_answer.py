def filter_chars(s):
    filtered = ''
    for i, c in enumerate(s):
        if 42 < i < 68 and 't' < c < 'x' or (i < 42 or i >= 68):
            filtered += c
    return filtered