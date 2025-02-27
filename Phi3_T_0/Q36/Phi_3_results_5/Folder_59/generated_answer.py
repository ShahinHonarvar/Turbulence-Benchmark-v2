def filter_chars(s):
    for i in range(3, 8):
        if '?' < s[i] < 'k':
            s = s.replace(s[i], '')
    return s