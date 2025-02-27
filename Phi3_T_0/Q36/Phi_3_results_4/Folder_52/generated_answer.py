def filter_chars(s):
    for i in range(50, 57):
        if 'I' < chr(i) < 'a':
            s = s.replace(chr(i), '')
    return s