def filter_chars(s):
    for char_code in range(170, 196):
        char = chr(char_code)
        s = s.replace(char, '')
    return s