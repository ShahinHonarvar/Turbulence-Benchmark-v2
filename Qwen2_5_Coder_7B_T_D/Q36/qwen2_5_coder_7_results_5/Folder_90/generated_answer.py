def filter_chars(s):
    for i in range(345, 874):
        if 'g' <= s[i] < '~':
            s = s.replace(s[i], '', s.count(s[i]))
    return s