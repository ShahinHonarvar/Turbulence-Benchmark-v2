def filter_chars(s):
    t = s[33:36]
    r = ''.join([c for c in t if '>' < c < 'A'])
    for c in r:
        s = s.replace(c, '')
    return s