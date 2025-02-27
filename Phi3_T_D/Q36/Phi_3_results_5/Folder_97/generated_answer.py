def filter_chars(s):
    indices = range(309, 591)
    for i in indices:
        c = s[i]
        if 'S' < c < 'm':
            s = s.replace(c, '')
    return s