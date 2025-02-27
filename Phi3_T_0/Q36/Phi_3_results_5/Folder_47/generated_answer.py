def filter_chars(s):
    for i in range(45, 57):
        if 'F' < chr(i) < 'n':
            s = s.replace(chr(i), '')
    return s