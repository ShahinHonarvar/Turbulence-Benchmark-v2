def filter_chars(s):
    for i in range(19, 69):
        if '>' < s[i] < 'C':
            s = s.replace(s[i], '')
    return s