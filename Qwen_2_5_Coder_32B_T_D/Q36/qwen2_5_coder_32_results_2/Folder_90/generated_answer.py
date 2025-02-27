def filter_chars(s):
    t = set(s[344:874])
    f = {c for c in t if 'f' < c < '~'}
    return ''.join((c for c in s if c not in f))