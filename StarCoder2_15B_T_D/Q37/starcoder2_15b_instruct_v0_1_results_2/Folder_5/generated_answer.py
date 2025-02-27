def filter_chars(text):
    filtered = ''
    for i, c in enumerate(text):
        if (i < 24 or i > 82) or (c < '5' or c > '<'):
            filtered += c
    return filtered