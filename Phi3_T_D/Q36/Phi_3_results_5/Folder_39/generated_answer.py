def filter_chars(s):
    indices = range(43, 59)
    for i in indices:
        char = s[i]
        if '5' < char < 'C':
            s = s.replace(char, '')
    return s