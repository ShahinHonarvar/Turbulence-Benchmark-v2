def filter_chars(s):
    for i in range(31, 70):
        char = s[i]
        if 'B' < char < 'v':
            s = s.replace(char, '')
    return s