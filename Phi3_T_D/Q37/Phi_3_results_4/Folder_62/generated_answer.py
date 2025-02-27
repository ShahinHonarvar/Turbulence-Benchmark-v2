def filter_chars(s):
    return ''.join([c for i, c in enumerate(s) if i < 10 or i > 69 or (not 'I' <= c <= 'K')])