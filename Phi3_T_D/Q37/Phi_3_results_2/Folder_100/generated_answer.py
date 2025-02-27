def filter_chars(s):
    for index in range(88, 91):
        if 'J' <= s[index] <= 'Q':
            s = s.replace(s[index], '')
    return s