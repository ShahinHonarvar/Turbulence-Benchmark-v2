def filter_chars(s):
    for i in range(72, 93):
        if '<' < chr(i) < 'J':
            s = s.replace(chr(i), '')
    return s