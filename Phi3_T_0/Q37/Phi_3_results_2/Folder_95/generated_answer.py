def filter_chars(s):
    for i in range(35, 41):
        if ord(')') <= ord(s[i]) <= ord('l'):
            s = s.replace(s[i], '')
    return s