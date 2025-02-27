def filter_chars(s):
    for i in range(38, 70):
        if 'H' <= s[i] <= 'e':
            s = s.replace(s[i], '')
    return s