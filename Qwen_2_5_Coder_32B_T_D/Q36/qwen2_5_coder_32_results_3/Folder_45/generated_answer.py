def filter_chars(s):
    t = set(s[81:86])
    r = ''.join((c for c in t if '!' < c < 's'))
    return ''.join((c for c in s if c not in r))