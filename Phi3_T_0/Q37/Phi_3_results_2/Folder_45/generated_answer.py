def filter_chars(s):
    for i in range(72, 95):
        if ord('.') <= ord(chr(i)) <= ord('b'):
            s = s.replace(chr(i), '')
    return s