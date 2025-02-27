def filter_chars(s):
    for c in s[318:337]:
        if 'B' < c < 'z':
            s = s.replace(c, '')
    return s