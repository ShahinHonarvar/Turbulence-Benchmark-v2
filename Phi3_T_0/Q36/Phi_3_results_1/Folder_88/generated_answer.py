def filter_chars(s):
    for i in range(78, 81):
        if 'S' < s[i] < '[':
            s = s.replace(s[i], '')
    return s