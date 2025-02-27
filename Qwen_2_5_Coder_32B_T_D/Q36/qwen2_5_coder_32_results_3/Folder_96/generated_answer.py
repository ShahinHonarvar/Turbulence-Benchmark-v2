def filter_chars(s):
    t = set(s[38:81])
    r = {c for c in t if '.' < c < '^'}
    return ''.join((c for c in s if c not in r))