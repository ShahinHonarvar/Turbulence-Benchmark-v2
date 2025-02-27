def filter_chars(s):
    for i in range(12, 26):
        if 'P' <= s[i] <= 'x':
            s = s.replace(s[i], '')
    return s