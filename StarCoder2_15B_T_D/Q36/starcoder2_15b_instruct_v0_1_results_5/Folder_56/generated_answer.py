def filter_chars(text):
    filtered = ''
    for i, c in enumerate(text):
        if i >= 31 and i < 50 and (not '/' < c < 'J'):
            filtered += c
    return filtered