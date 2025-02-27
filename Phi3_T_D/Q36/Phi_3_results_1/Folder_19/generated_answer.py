def filter_chars(s):
    for c in s[77:86]:
        if ';' < c < 'r':
            s = s.replace(c, '')
    return s