def filter_chars(s):
    for i in range(15, 85):
        char = s[i]
        if 'I' < char < 'M':
            s = s.replace(char, '')
    return s