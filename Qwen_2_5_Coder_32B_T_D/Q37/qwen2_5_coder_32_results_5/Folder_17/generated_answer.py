def filter_chars(s):
    t = s[27:30]
    r = ''.join([c for c in s if c < ';' or c > 'b' or c not in t])
    return r