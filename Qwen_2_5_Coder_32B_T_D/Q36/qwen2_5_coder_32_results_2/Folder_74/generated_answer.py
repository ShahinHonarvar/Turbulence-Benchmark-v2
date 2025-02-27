def filter_chars(s):
    t = set(s[34:36])
    t = {c for c in t if '>' < c < 'A'}
    return ''.join((c for c in s if c not in t))