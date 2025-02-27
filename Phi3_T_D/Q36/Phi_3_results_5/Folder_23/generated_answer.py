def filter_chars(s):
    for i in range(21, 25):
        if '5' < s[i] < '}':
            s = s.replace(s[i], '')
    return s