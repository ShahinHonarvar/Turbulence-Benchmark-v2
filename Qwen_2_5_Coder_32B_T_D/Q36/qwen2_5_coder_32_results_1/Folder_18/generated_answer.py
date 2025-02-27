def filter_chars(s):
    t = s[587:648]
    chars = set((c for c in t if ',' < c < 'c'))
    return ''.join((c for c in s if c not in chars))