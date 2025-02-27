def filter_chars(s):
    for char in range(82, 89):
        if 'f' < chr(char) < '{':
            s = s.replace(chr(char), '')
    return s