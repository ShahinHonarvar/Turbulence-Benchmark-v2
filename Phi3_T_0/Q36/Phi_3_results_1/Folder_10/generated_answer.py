def filter_chars(s):
    for i in range(35, 60):
        if '!' < s[i] < 'B':
            s = s.replace(s[i], '')
    return s