def filter_chars(s):
    for c in s[2:10]:
        if '8' < c < 'm':
            s = s.replace(c, '')
    return s