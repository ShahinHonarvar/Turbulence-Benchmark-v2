def filter_chars(s):
    for i in range(55, 66):
        if 'f' < chr(i) < '|':
            s = s.replace(chr(i), '')
    return s