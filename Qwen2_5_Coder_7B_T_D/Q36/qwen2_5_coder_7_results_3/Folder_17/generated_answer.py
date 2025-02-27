def filter_chars(s):
    for c in range(18, 95):
        if 'K' < chr(c) < 'a':
            s = s.replace(chr(c), '')
    return s