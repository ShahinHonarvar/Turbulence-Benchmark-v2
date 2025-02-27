def filter_chars(s):
    for i, c in enumerate(s):
        if 27 < i < 75 and ord('A') < ord(c) < ord('i'):
            s = s.replace(c, '')
    return s