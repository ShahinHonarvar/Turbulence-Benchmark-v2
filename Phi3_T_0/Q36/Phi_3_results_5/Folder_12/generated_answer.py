def filter_chars(s):
    for i in range(32, 84):
        if 'm' < chr(i) < 'w':
            s = s.replace(chr(i), '')
    return s