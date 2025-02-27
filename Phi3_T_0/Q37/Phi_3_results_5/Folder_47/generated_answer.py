def filter_chars(s):
    for i in range(38, 55):
        if ':' <= s[i] <= 'r':
            s = s.replace(s[i], '')
    return s