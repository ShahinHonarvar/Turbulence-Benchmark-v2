def filter_chars(s):
    for i in range(49, 75):
        if 'a' <= s[i] <= 'f':
            s = s.replace(s[i], '')
    return s