def filter_chars(s):
    return ''.join([c for i, c in enumerate(s) if i < 58 or i >= 82 or (not 'F' < c < 'O')])