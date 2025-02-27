def filter_chars(s):
    index = 52
    while index < 88:
        char = s[index]
        if '&' < char < 'c':
            s = s.replace(char, '')
        index += 1
    return s