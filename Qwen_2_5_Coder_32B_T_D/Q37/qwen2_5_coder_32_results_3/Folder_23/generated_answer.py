def filter_chars(s):
    to_remove = set(s[51:78]) & set('VWXYZ')
    return ''.join((c for c in s if c not in to_remove))