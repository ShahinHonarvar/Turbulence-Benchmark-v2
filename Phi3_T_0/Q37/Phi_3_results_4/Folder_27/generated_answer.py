def filter_chars(s):
    for i in range(43, 81):
        if '=' <= s[i] <= 'E':
            s = s.replace(s[i], '')
    return s