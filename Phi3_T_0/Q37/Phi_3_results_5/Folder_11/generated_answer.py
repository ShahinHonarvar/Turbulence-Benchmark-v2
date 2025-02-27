def filter_chars(s):
    for i in range(29, 98):
        if '-' <= chr(i) <= 'n':
            s = s.replace(chr(i), '')
    return s