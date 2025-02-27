def filter_chars(s):
    for i in range(770, 971):
        if 'A' <= s[i] <= 'D':
            s = s.replace(s[i], '')
    return s