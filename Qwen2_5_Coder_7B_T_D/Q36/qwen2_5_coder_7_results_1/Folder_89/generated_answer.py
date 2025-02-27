def filter_chars(s):
    for char in range(57, 69):
        if '(' < chr(char) < 'W':
            s = s.replace(chr(char), '')
    return s