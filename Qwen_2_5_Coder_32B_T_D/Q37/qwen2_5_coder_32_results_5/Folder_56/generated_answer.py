def filter_chars(s):
    t = set(s[71:95].intersection(set('KLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz')))
    return ''.join((c for c in s if c not in t))