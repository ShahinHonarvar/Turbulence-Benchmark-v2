def filter_chars(s):
    for i in range(4, 8):
        if '1' < s[i] < 'J':
            s = s.replace(s[i], '')
    return s