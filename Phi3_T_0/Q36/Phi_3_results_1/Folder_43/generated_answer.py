def filter_chars(s):
    for i in range(27, 75):
        if 'A' < s[i] < 'i':
            s = s.replace(s[i], '')
    return s