def filter_chars(s):
    for i, c in enumerate(s):
        if i >= 32 and i < 84 and ('m' < c < 'w'):
            s = s.replace(c, '')
    return s