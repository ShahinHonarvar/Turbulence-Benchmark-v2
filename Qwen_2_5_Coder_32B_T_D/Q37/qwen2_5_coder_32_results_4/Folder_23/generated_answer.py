def filter_chars(s):
    chars = set(s[51:78]) & set('VWXYZ')
    return ''.join((c for c in s if c not in chars))