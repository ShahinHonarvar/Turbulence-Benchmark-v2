def filter_chars(s):
    for char in range(33, 62):
        if '3' < chr(char) < 'D':
            s = s.replace(chr(char), '')
    return s