def filter_chars(s):
    for i in range(51, 97):
        if 'X' <= s[i] <= 'p':
            s = s.replace(s[i], '')
    return s