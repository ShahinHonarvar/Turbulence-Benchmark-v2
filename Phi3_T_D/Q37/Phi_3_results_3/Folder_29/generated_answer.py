def filter_chars(s):
    for i in range(12, 89):
        if '&' <= s[i] <= 'v':
            s = s.replace(s[i], '')
    return s