def filter_chars(s):
    for i in range(81, 86):
        if ord('!') < ord(s[i]) < ord('s'):
            s = s.replace(s[i], '')
    return s