def filter_chars(string):
    filtered = ''
    for i, c in enumerate(string):
        if (i < 513 or i > 877) or (c < '?' or c > 'n'):
            filtered += c
    return filtered