def filter_chars(s):
    for i in range(4, 4 + 1):
        if '7' <= s[i] <= 'o':
            s = s.replace(s[i], '')
    return s