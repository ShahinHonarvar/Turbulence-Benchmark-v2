def filter_chars(s):
    for i in range(10, 53):
        if '@' <= s[i] <= 'T':
            s = s.replace(s[i], '')
    return s