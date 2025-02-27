def filter_chars(s):
    for i in range(42, 67):
        if '6' < s[i] < 'g':
            s = s.replace(s[i], '')
    return s