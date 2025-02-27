def filter_chars(s):
    for i in range(50, 92):
        if 'A' < chr(i) < 'Q':
            s = s.replace(chr(i), '')
    return s