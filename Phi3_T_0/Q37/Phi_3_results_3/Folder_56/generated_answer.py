def filter_chars(s):
    for i in range(71, 95):
        if 'K' <= chr(i) <= 'a':
            s = s.replace(chr(i), '')
    return s