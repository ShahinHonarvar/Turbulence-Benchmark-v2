def filter_chars(s):
    for i in range(1, 6):
        if ord(s[i]) > ord(','):
            s = s.replace(s[i], '')
    return s