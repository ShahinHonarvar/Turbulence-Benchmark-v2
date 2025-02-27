def filter_chars(s):
    for i in range(27, 86):
        if 'c' <= chr(i) <= 'i':
            s = s.replace(chr(i), '')
    return s