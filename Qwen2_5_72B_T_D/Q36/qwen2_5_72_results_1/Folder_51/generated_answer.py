def filter_chars(s):
    for i in range(58, 81):
        char = s[i]
        if '5' < char < '>':
            s = s.replace(char, '')
    return s