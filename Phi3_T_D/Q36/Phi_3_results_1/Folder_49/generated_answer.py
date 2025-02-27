def filter_chars(s):
    return ''.join([c for i, c in enumerate(s) if i < 46 or i >= 91 or (not 'D' < c < 'H')])