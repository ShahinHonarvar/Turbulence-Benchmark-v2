def filter_chars(s):
    t = set(s[55:80])
    r = [c for c in t if 'S' < c < 's']
    return ''.join((c for c in s if c not in r))