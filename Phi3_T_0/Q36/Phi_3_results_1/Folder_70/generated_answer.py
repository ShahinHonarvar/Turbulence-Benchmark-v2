def filter_chars(s):
    for i in range(170, 195):
        if '!' < chr(i) < '}':
            s = s.replace(chr(i), '')
    return s