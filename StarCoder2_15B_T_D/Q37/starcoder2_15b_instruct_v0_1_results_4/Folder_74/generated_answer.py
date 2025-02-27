def filter_chars(s):
    return ''.join([c for i, c in enumerate(s) if i < 19 or i > 32 or c < 'f' or (c > 'o')])