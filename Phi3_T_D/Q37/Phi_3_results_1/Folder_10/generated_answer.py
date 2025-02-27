def filter_chars(s):
    for i in range(63, 85):
        char = chr(i)
        s = s.replace(char, '')
    return s