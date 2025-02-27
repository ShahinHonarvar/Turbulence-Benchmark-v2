def filter_chars(s):
    for c in range(343, 665):
        if '%' < s[c] < 'U':
            s = s.replace(s[c], '')
    return s