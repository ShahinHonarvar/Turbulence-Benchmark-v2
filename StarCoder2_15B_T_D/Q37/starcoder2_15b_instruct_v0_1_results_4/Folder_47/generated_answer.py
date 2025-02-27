def filter_chars(string):
    filtered = ''
    for i, c in enumerate(string):
        if not (38 <= i <= 54 and ':' <= c <= 'r'):
            filtered += c
    return filtered