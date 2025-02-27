def filter_chars(s):
    for i in range(43, 83, 1):
        if ':' < s[i] < 'Q':
            s = s.replace(s[i], '')
    return s