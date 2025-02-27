def filter_chars(s):
    for i in range(17, 64):
        if 'O' <= s[i] <= '^':
            s = s.replace(s[i], '')
    return s