def filter_chars(s):
    for i in range(2, 8):
        char = s[i]
        if 'h' < char < 'k':
            s = s.replace(char, '')
    return s