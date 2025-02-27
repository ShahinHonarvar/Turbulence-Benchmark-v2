def filter_chars(s):
    if len(s) < 81:
        return s
    for i in range(58, 81):
        if '5' < s[i] < '>':
            s = s.replace(s[i], '')
    return s