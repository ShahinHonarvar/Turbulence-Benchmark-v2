def filter_chars(s):
    for i in range(81, 89):
        char = s[i]
        if 'f' < char < '{':
            s = s.replace(char, '')
    return s