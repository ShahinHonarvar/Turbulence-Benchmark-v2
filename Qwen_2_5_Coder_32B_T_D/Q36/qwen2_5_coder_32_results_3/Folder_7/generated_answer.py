def filter_chars(s):
    t = s[502:946]
    r = set((c for c in t if 'W' < c < 'y'))
    return ''.join((c for c in s if c not in r))