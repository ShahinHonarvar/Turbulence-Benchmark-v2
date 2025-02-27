def filter_chars(text):
    filtered = ''
    for i, c in enumerate(text):
        if i < 24 or i >= 37 or c <= 'A' or (c >= 'h'):
            filtered += c
    return filtered