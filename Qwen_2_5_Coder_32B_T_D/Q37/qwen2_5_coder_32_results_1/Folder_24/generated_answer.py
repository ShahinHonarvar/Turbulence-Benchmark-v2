def filter_chars(s):
    t = s[36:80]
    r = ''.join({c for c in t if '2' <= c <= 's'})
    return ''.join((c for c in s if c not in r))