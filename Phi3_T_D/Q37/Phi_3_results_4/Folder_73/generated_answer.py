def filter_chars(s):
    for i in range(22, 86):
        if 'g' <= s[i] <= 'l':
            s = s.replace(s[i], '')
    return s