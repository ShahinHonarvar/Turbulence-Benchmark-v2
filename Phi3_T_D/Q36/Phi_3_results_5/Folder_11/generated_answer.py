def filter_chars(s):
    for i in range(86, 93):
        if 'E' < chr(i) < '~':
            s = s.replace(chr(i), '')
    return s