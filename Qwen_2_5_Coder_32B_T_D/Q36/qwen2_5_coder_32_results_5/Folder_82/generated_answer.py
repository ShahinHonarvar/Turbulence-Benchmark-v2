def filter_chars(s):
    t = set(s[70:97])
    r = [c for c in t if 'V' < c < 'j']
    return ''.join([c for c in s if c not in r])