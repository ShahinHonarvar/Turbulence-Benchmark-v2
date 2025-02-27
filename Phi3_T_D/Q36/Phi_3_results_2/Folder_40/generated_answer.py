def filter_chars(s):
    for i in range(1, 7):
        if ord('-') < ord(s[i]) < ord('L'):
            s = s.replace(s[i], '')
    return s