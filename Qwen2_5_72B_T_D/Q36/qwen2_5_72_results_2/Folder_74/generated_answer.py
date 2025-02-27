def filter_chars(s):
    for i in range(33, 37):
        if '>' < s[i] < 'A':
            s = s.replace(s[i], '')
    return s