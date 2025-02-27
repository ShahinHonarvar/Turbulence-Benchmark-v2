def filter_chars(s):
    return ''.join((c for i, c in enumerate(s) if i < 41 or i > 64 or c < 'K' or (c > ']')))