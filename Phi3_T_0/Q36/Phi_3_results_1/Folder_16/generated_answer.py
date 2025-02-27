def filter_chars(s):
    for i in range(331, 713):
        if 'M' < s[i] < '_':
            s = s.replace(s[i], '')
    return s