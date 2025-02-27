def filter_chars(s):
    for i in range(25, 97):
        c = chr(i)
        if 'm' <= c <= 'w':
            s = s.replace(c, '')
    return s