def filter_chars(s):
    for i in range(38, 100):
        if chr(i) >= 'A' and chr(i) <= 'Q':
            s = s.replace(chr(i), '')
    return s