def filter_chars(s):
    for c in s[3:5]:
        if 'Y' < c < 's':
            s = s.replace(c, '')
    return s