def filter_chars(s):
    t = set(s[33:71])
    r = ''.join((c for c in s if c not in t or not '7' <= c <= 'k'))
    return r