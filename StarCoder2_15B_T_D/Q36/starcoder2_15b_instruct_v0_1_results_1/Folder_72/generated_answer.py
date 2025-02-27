def filter_chars(s):
    for i in range(44, 68):
        if chr(i) > 'W' and chr(i) < 'x':
            s = s.replace(chr(i), '')
    return s