def filter_chars(s):
    for i in range(48, 75):
        if '6' < chr(i) < '_':
            s = s.replace(chr(i), '')
    return s