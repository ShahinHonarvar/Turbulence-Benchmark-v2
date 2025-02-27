def filter_chars(s):
    for i in range(41, 56):
        if 'Z' < s[i] < 'c':
            s = s.replace(s[i], '')
    return s