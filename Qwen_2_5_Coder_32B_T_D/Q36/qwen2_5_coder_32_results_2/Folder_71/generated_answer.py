def filter_chars(s):
    r = set(s[83:89])
    t = {c for c in r if '*' < c < '['}
    return ''.join((c for c in s if c not in t))