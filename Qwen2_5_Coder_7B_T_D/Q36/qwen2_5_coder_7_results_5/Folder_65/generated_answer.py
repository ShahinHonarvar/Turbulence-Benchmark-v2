def filter_chars(s):
    range_chars = set('GHIJK')
    return ''.join((c for c in s if c not in range_chars))