def filter_chars(s):
    for i in range(48, 75):
        if '0' < chr(i) < '_':
            s = s.replace(chr(i), '')
    return s