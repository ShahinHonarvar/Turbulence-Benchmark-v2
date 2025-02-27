def filter_chars(s):
    for i in range(348, 853):
        c = s[i]
        if 'J' <= c <= 'b':
            s = s.replace(c, '')
    return s