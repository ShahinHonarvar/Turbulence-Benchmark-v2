def filter_chars(s):
    for i in range(46, 91):
        if 'D' < chr(i) < 'H':
            s = s.replace(chr(i), '')
    return s