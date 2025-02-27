def filter_chars(s):
    t = set(s[17:64])
    r = {c for c in t if 'O' <= c <= '^'}
    return ''.join((c for c in s if c not in r))