def filter_chars(s):
    if len(s) < 88:
        return s
    for c in s[52:88]:
        if '&' < c < 'c':
            s = s.replace(c, '')
    return s