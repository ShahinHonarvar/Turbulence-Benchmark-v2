def filter_chars(s):
    a = ''.join(s[38:81])
    r = ''.join((c for c in a if '.' < c < '^'))
    for c in r:
        s = s.replace(c, '')
    return s