def filter_chars(s):
    t = s[7:10]
    r = set((c for c in t if '6' <= c <= 'w'))
    return ''.join((c for c in s if c not in r))