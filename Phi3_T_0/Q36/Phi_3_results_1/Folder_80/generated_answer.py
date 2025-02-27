def filter_chars(s):
    for i in range(54, 92):
        if 'J' < chr(i) < 'X':
            s = s.replace(chr(i), '')
    return s