def filter_chars(s):
    for index in range(10, 15):
        char = s[index]
        if 't' < char < 'v':
            s = s.replace(char, '')
    return s