def filter_chars(s):
    for i in range(32, 61):
        if '3' < chr(i) < 'D':
            s = s.replace(chr(i), '')
    return s