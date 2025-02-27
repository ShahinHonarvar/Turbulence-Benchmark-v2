def filter_chars(s):
    for c in s[29:33]:
        if '%' < c and c < 'a':
            s = s.replace(c, '')
    return s