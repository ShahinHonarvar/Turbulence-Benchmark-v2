def filter_chars(s):
    for i in range(70, 75):
        char = s[i]
        if 'A' < char < 'U':
            s = s.replace(char, '')
    return s