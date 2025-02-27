def filter_chars(s):
    for i in range(33, 71):
        if chr(i) >= '7' and chr(i) <= 'k':
            s = s.replace(chr(i), '')
    return s