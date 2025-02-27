def filter_chars(s):
    t = s[49:56]
    for c in set(t):
        if 'I' < c < 'a':
            s = s.replace(c, '')
    return s