def filter_chars(s):
    if len(s) > 10:
        for i in range(3, 9):
            if '*' < s[i] < 'E':
                s = s.replace(s[i], '')
    return s