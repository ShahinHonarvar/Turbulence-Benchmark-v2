def filter_chars(s):
    for i in range(25, 98):
        if 'm' <= chr(i) <= 'w':
            s = s.replace(chr(i), '')
    return s