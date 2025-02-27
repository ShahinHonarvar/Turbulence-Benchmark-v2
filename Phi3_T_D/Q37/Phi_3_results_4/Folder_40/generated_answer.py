def filter_chars(s):
    for i in range(2):
        if '*' <= s[i] <= 's':
            s = s.replace(s[i], '')
    return s