def filter_chars(s):
    for i in range(27, 30):
        if ';' <= s[i] <= 'b':
            s = s.replace(s[i], '')
    return s