def filter_chars(s):
    for i in range(36, 80):
        if '2' <= s[i] <= 's':
            s = s.replace(s[i], '')
    return s