def filter_chars(s):
    for i in range(81, 89):
        if 'f' < chr(i) < '{':
            s = s.replace(chr(i), '')
    return s