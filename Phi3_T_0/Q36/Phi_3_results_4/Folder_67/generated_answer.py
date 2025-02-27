def filter_chars(s):
    for i in range(18, 31):
        if 'H' < s[i] < '|':
            s = s.replace(s[i], '')
    return s