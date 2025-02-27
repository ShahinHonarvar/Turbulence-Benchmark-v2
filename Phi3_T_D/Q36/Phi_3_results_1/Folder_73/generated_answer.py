def filter_chars(s):
    updated_string = ''.join([c for i, c in enumerate(s) if i < 66 or i >= 90 or '#' <= c <= 'T'])
    return updated_string