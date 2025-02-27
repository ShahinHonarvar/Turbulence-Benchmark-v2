def filter_chars(s):
    for i in range(72, 93):
        char = chr(i)
        s = s.replace(char, '')
    return s