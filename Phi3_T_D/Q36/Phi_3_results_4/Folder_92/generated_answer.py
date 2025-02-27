def filter_chars(s):
    for i in range(1, 6):
        if ',<f' < s[i] < 'f':
            s = s.replace(s[i], '')
    return s