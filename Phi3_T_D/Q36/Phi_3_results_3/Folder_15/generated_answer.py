def filter_chars(s):
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    return ''.join([c for i, c in enumerate(s) if not (2 < i < 7 and 'h' < c < 'k')])