def filter_chars(s):
    t = set(s[56:86])
    r = ''.join([c for c in t if '+' < c < 'w'])
    return ''.join([c for c in s if c not in r])