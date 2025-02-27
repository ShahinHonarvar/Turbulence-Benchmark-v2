def filter_chars(s):
    for i in range(55, 84):
        c = s[i]
        if ';' < c < 'z':
            s = s.replace(c, '')
    return s