def filter_chars(s):
    for i in range(48, 75):
        c = chr(i)
        if '6' < c < '_':
            s = s.replace(c, '')
    return s