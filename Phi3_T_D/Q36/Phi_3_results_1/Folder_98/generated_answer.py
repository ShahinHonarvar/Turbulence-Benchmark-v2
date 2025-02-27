def filter_chars(s):
    for i in range(4, 8):
        char = s[i]
        if '1' < char < 'J':
            s = s.replace(char, '')
    return s