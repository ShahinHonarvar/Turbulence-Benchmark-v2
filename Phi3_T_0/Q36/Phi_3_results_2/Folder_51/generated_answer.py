def filter_chars(s):
    for i in range(58, 81):
        if '5' < s[i] < '>':
            s = s.replace(s[i], '')
    return s