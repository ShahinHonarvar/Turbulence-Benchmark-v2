def filter_chars(s):
    for i in range(69, 97):
        if 'V' < chr(i) < 'j':
            s = s.replace(chr(i), '')
    return s