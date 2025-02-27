def filter_chars(s):
    t = set(s[72:95])
    r = ''.join([c for c in t if '.' <= c <= 'b'])
    return ''.join([c for c in s if c not in r])