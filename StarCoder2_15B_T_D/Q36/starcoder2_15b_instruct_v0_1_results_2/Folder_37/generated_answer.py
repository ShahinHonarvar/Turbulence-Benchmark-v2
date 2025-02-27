def filter_chars(s):
    for i in range(44, 59):
        c = chr(i)
        if c > '/' and c < '6':
            s = s.replace(c, '')
    return s