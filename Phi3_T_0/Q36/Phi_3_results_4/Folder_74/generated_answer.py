def filter_chars(s):
    for i in range(33, 36):
        if '>' < chr(i) < 'A':
            s = s.replace(chr(i), '')
    return s