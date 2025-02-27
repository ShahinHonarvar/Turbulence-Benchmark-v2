def filter_chars(s):
    for i in range(49, 56):
        char = chr(i)
        s = s.replace(char, '')
    return s