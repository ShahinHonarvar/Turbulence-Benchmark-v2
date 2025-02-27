def filter_chars(s):
    for i in range(19, 34):
        if 'S' <= s[i] <= '{':
            s = s.replace(s[i], '')
    return s