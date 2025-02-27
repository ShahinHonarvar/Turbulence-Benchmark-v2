def filter_chars(s):
    for i in range(10, 79):
        if '?' < s[i] < 'm':
            s = s.replace(s[i], '')
    return s