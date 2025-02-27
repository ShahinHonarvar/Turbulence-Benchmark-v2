def filter_chars(s):
    for i in range(69, 97):
        s = s.replace(chr(i), '')
    return s