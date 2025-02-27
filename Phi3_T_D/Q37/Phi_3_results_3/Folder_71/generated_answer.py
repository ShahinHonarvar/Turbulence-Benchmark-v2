def filter_chars(s):
    k = 'k'
    return ''.join([c for i, c in enumerate(s) if i < 32 or i > 46 or (not '0' <= c <= k)])