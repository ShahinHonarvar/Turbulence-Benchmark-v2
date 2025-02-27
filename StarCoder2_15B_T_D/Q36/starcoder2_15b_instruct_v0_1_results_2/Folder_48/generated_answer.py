def filter_chars(s):
    for i in range(154, 222):
        if chr(i) > 'A' and chr(i) < 'f':
            s = s.replace(chr(i), '')
    return s