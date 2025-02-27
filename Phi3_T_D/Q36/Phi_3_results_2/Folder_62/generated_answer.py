def filter_chars(s):
    for i in range(64, 90):
        c = chr(i)
        if '*' < c < 'w':
            s = s.replace(c, '')
    return s