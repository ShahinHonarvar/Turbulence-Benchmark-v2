def filter_chars(s):
    r = set(s[318:337])
    r = {c for c in r if 'B' < c < 'z'}
    return ''.join((c for c in s if c not in r))