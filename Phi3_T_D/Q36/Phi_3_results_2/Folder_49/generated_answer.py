def filter_chars(s):
    for c in s[46:91]:
        if 'D' < c < 'H':
            s = s.replace(c, '')
    return s